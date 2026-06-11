import os
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

def main():
    print("=== [DINKES SYSTEM] Memulai Proses Training AI & Validasi Berkala ===")
    
    if not os.path.exists('data/dataset.csv'):
        print("Error: Jalankan download_data.py terlebih dahulu!")
        return
        
    df = pd.read_csv('data/dataset.csv')
    
    # Fitur input klinis + fitur ekstraksi wajah
    X = df[['umur', 'jenis_kelamin', 'status_hamil', 'bmi', 
            'mudah_lelah', 'pusing', 'sesak_napas', 'jantung_berdebar', 
            'heart_rate', 'spo2', 'suhu_tubuh', 'nilai_kamera_pucat']]
    y = df['anemia']
    
    # Split data 80:20
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Menggunakan 100-150 estimator pohon keputusan (Setara keandalan 100 epoch di DL)
    print("Mengonfigurasi model utama Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, class_weight='balanced')
    
    # === SISTEM CEK BERKALA (K-FOLD CROSS VALIDATION) ===
    print("Melakukan pengecekan berkala (5-Fold Cross Validation) untuk stabilitas matriks...")
    skor_berkala = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    print(f"-> Konsistensi Akurasi Tiap Siklus Cek: {skor_berkala}")
    print(f"-> Rata-rata Akurasi Validasi Berkala: {skor_berkala.mean() * 100:.2f}%")
    
    # Training Akhir
    model.fit(X_train, y_train)
    
    # Evaluasi Matriks Ketat untuk Dinas Kesehatan
    y_pred = model.predict(X_test)
    print("\n================== GAP MATRIKS EVALUASI KLINIS ==================")
    print(f"Akurasi Final Pengujian: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\nLaporan Klasifikasi Detail:")
    print(classification_report(y_test, y_pred, target_names=['Normal (Sehat)', 'Risiko Anemia']))
    
    # Cek Confusion Matrix (Memastikan deteksi tidak meleset/nyasar)
    cm = confusion_matrix(y_test, y_pred)
    print(f"Matriks Meleset (False Negative): {cm[1][0]} Pasien")
    print(f"Matriks Tepat Sasaran (True Positive): {cm[1][1]} Pasien")
    
    # Simpan model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/model.pkl')
    print("\n✅ Model Ter-Validasi Selesai Disimpan!")

if __name__ == '__main__':
    main()