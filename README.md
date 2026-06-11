<div align="center">

# 🩸 ANEMIA-GUARD AI

### Clinical Intelligence Platform for Early Anemia Risk Screening

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=24&duration=3000&pause=1000&center=true&vCenter=true&width=900&lines=Hybrid+AI+for+Early+Anemia+Risk+Screening;Computer+Vision+%2B+Machine+Learning+%2B+IoT;Clinical+Decision+Support+Prototype;Built+for+Healthcare+Innovation"/>

**Precision • Accountability • Clinical Intelligence**

</div>

---

# Executive Summary

ANEMIA-GUARD AI merupakan platform **Hybrid Artificial Intelligence** yang dirancang untuk membantu proses screening dini risiko anemia melalui kombinasi:

- Deep Learning
- Machine Learning
- Computer Vision
- Clinical Analytics
- IoT Integration

Platform ini dikembangkan sebagai fondasi menuju sistem **Clinical Decision Support System (CDSS)** modern yang dapat digunakan dalam penelitian, pendidikan, program kesehatan preventif, serta pengembangan teknologi kesehatan digital.

> **Medical Disclaimer**
>
> Sistem ini merupakan alat bantu screening risiko awal dan tidak dimaksudkan sebagai alat diagnosis medis resmi. Seluruh hasil harus dikonfirmasi melalui pemeriksaan klinis dan laboratorium oleh tenaga kesehatan profesional.

---

# Why This Project Matters

Anemia masih menjadi salah satu tantangan kesehatan masyarakat dengan dampak signifikan terhadap:

- Ibu Hamil
- Remaja Putri
- Anak-anak
- Lansia
- Kelompok Rentan

Deteksi dini memungkinkan intervensi lebih cepat sehingga dapat membantu:

✅ Mengurangi risiko komplikasi kehamilan

✅ Mendukung pencegahan stunting

✅ Memperkuat program kesehatan preventif

✅ Meningkatkan kualitas monitoring populasi

---

# Core Technologies

| Layer | Technology |
|---------|---------|
| Frontend Dashboard | Streamlit |
| Programming Language | Python |
| Computer Vision | OpenCV |
| Deep Learning | PyTorch |
| CNN Backbone | VGG16 |
| Machine Learning | Random Forest |
| Data Analytics | Pandas |
| Numerical Computing | NumPy |
| Model Storage | Joblib |
| Excel Export | OpenPyXL |

---

# System Architecture

```text
Camera Input
      │
      ▼
OpenCV Face Detection
      │
      ▼
VGG16 Feature Extraction
      │
      ▼
Visual Biomarker Vector
      │
      ├──── Clinical Symptoms
      │
      ├──── Demographic Data
      │
      └──── IoT Sensor Data
                │
                ▼
      Random Forest Classifier
                │
                ▼
       Risk Prediction Engine
                │
                ▼
      Clinical Recommendation
```

---

# Hybrid AI Framework

## Deep Learning Layer

Menggunakan model VGG16 pretrained sebagai feature extractor untuk memperoleh representasi visual wajah yang berkaitan dengan karakteristik pucat (pallor).

### Objective

- Face Analysis
- Pallor Assessment
- Feature Embedding
- Visual Biomarker Extraction

---

## Machine Learning Layer

Output feature visual digabungkan dengan:

- Usia
- Jenis Kelamin
- Gejala Klinis
- Data Sensor
- Riwayat Kesehatan

Kemudian diproses oleh:

```text
Random Forest Classifier
```

untuk menghasilkan probabilitas risiko anemia.

---

# Clinical Risk Classification

| Level | Probability | Status |
|---------|---------|---------|
| 🟢 Low Risk | <35% | Monitoring |
| 🟡 Moderate Risk | 35-69% | Preventive Intervention |
| 🔴 High Risk | ≥70% | Immediate Referral |

---

# IoT Integration Roadmap

Target integrasi hardware:

| Device | Function |
|---------|---------|
| ESP32 | Edge Processing |
| MAX30102 | Heart Rate & SpO₂ |
| MLX90614 | Body Temperature |
| Camera Module | Facial Analysis |

---

# Validation Framework

Model dievaluasi menggunakan:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC
- 5-Fold Cross Validation

Target performa:

| Metric | Target |
|---------|---------|
| Accuracy | ≥ 85% |
| Recall | ≥ 85% |
| Precision | ≥ 80% |
| F1 Score | ≥ 80% |

---

# Project Structure

```text
anemia_guard_ai/
│
├── app.py
├── training.py
├── download_data.py
├── requirements.txt
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── model.pkl


---

# Installation

## Clone Repository

```bash
git clone https://github.com/kyyyyyykyyy/PENDETEKSI-ANEMIA.git
cd anemia-guard-ai
```

## Create Virtual Environment

```bash
py -m venv .venv
```

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
py -m pip install --upgrade pip
```

```bash
py -m pip install streamlit pandas numpy scikit-learn joblib matplotlib opencv-python Pillow torch torchvision openpyxl --prefer-binary
```

---

# Run Application

## Download Dataset

```bash
py download_data.py
```

## Train Model

```bash
py training.py
```

## Launch Dashboard

```bash
py -m streamlit run app.py
```

---

# Security & Governance

Future development targets:

- Patient Data Anonymization
- Audit Logging
- Role-Based Access Control
- Encryption at Rest
- Encryption in Transit
- Clinical Governance Review

---

# Research & Innovation

This project combines:

- Artificial Intelligence
- Clinical Informatics
- Medical Decision Support
- Computer Vision
- Preventive Healthcare

to explore practical approaches for early anemia risk screening.

---

# Roadmap

### Phase I
- Core Dashboard
- Face Analysis
- Machine Learning Engine

### Phase II
- ESP32 Integration
- Sensor Connectivity
- Real-Time Processing

### Phase III
- Cloud Deployment
- Mobile Application
- Central Analytics Platform

### Phase IV
- Multi-Facility Deployment
- Federated Learning
- Research Collaboration

---

# License

MIT License

---

<div align="center">

## ⚖️ ANEMIA-GUARD AI

### Clinical Intelligence • Responsible Innovation • Healthcare Technology

*"Building trustworthy AI for preventive healthcare."*

</div>
