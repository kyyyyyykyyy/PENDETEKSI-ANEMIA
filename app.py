import streamlit as st
import pandas as pd
import numpy as np
import cv2
import joblib
import os

st.set_page_config(page_title="ANEMIA-GUARD AI - Dinkes Face Tracking", layout="wide")

@st.cache_resource
def load_anemia_model():
    return joblib.load('models/model.pkl') if os.path.exists('models/model.pkl') else None

model = load_anemia_model()

# Mengunduh database wajah cascade default OpenCV jika belum ada
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

st.title("🩸 ANEMIA-GUARD AI")
st.subheader("Sistem Screening Berbasis Biometrik Wajah & Validasi Matriks Klinis")
st.markdown("---")

col_input, col_output = st.columns([1, 1])
nilai_ekstraksi_kamera = 150 

with col_input:
    st.header("📸 1. Pemindaian Wajah & Deteksi Kepucatan Fisik")
    foto_user = st.camera_input("Posisikan Wajah Anda di Tengah Kamera")
    
    if foto_user is not None:
        file_bytes = np.asarray(bytearray(foto_user.read()), dtype=np.uint8)
        frame_bgr = cv2.imdecode(file_bytes, 1)
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        
        # PROSES DETEKSI WAJAH BERBASIS KOORDINAT
        gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) > 0:
            # Ambil koordinat wajah pertama yang dideteksi
            (x, y, w, h) = faces[0]
            # Potong gambar hanya di area wajah (ROI - Region of Interest)
            wajah_crop = frame_rgb[y:y+h, x:x+w]
            
            # Ekstraksi nilai hemoglobin visual (Rata-rata Intensitas Kemerahan Kulit Wajah)
            rata_merah = np.mean(wajah_crop[:, :, 0])
            nilai_ekstraksi_kamera = int(rata_merah)
            
            st.success(f"✅ Wajah Terdeteksi Berhasil! Indeks Kemerahan Kulit: {nilai_ekstraksi_kamera}")
            
            # Menampilkan area wajah yang berhasil di-scan oleh AI
            st.image(wajah_crop, caption="Area Wajah yang Dipindai AI", width=150)
        else:
            st.warning("⚠️ Wajah kurang jelas atau pencahayaan minim. Menggunakan deteksi standar global.")
            nilai_ekstraksi_kamera = int(np.mean(frame_rgb[:, :, 0]))

    st.markdown("---")
    st.header("📝 2. Rekam Medis & Hasil Sensor")
    with st.form("form_klinis"):
        umur = st.number_input("Usia Pasien", min_value=1, max_value=100, value=25)
        jk = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        hamil = st.selectbox("Status Kehamilan", ["Tidak", "Ya"])
        bb = st.number_input("Berat Badan (kg)", value=60.0)
        tb = st.number_input("Tinggi Badan (cm)", value=165.0)
        
        st.caption("Keluhan Pasien:")
        lelah = st.checkbox("Mudah lelah / lemas")
        pusing = st.checkbox("Sering pusing")
        sesak = st.checkbox("Ada sesak napas")
        debar = st.checkbox("Jantung berdebar")
        
        st.caption("Parameter IoT Hardware:")
        hr = st.slider("Heart Rate (BPM)", 50, 140, 80)
        spo2 = st.slider("SpO2 (%)", 85, 100, 98)
        suhu = st.slider("Suhu Tubuh (°C)", 35.5, 40.0, 36.4, step=0.1)
        
        btn_submit = st.form_submit_button("JALANKAN SCREENING DINAS KESEHATAN")

with col_output:
    st.header("📊 3. Laporan Keputusan Klinis")
    if btn_submit:
        if model is None:
            st.error("Model AI belum dilatih! Jalankan training.py terlebih dahulu.")
        else:
            bmi_kalkulasi = bb / ((tb / 100) ** 2)
            jk_bin = 1 if jk == "Perempuan" else 0
            hamil_bin = 1 if hamil == "Ya" else 0
            
            data_pasien = pd.DataFrame([[
                umur, jk_bin, hamil_bin, bmi_kalkulasi,
                1 if lelah else 0, 1 if pusing else 0, 1 if sesak else 0, 1 if debar else 0,
                hr, spo2, suhu, nilai_ekstraksi_kamera
            ]], columns=['umur', 'jenis_kelamin', 'status_hamil', 'bmi', 
                         'mudah_lelah', 'pusing', 'sesak_napas', 'jantung_berdebar', 
                         'heart_rate', 'spo2', 'suhu_tubuh', 'nilai_kamera_pucat'])
            
            skor_probabilitas = model.predict_proba(data_pasien)[0][1]
            
            if skor_probabilitas < 0.35:
                status_risiko = "RISIKO RENDAH (NORMAL)"
                warna_tema = "#2ecc71"
                rekomendasi = "Pasien dalam kondisi prima. Tetap pertahankan pola makan seimbang."
            elif 0.35 <= skor_probabilitas < 0.70:
                status_risiko = "RISIKO SEDANG (WASPADA)"
                warna_tema = "#e67e22"
                rekomendasi = "Terdeteksi indikasi anemia ringan. Berikan intervensi Tablet Tambah Darah (TTD)."
            else:
                status_risiko = "RISIKO TINGGI (BAHAYA)"
                warna_tema = "#e74c3c"
                rekomendasi = "Pasien darurat anemia klinis. Rujuk segera ke faskes terdekat untuk cek lab darah."
            
            st.markdown(f"""
            <div style="background-color: {warna_tema}; padding: 25px; border-radius: 12px; text-align: center; color: white;">
                <h1 style='margin:0; font-size:30px;'>{status_risiko}</h1>
                <h4 style='margin:5px 0 0 0;'>Tingkat Kepastian AI: {skor_probabilitas * 100:.1f}%</h4>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"📋 **Protokol Interventions Dinkes:**\n\n{rekomendasi}")
            
            st.subheader("Metrik Kesehatan Terkalkulasi:")
            m1, m2, m3 = st.columns(3)
            m1.metric("Skor BMI", f"{bmi_kalkulasi:.1f}")
            m2.metric("Indeks Merah Kulit", f"{nilai_ekstraksi_kamera}")
            m3.metric("Saturasi Oksigen", f"{spo2}%")
    else:
        st.info("Menunggu data dimasukkan untuk melakukan screening klinis.")