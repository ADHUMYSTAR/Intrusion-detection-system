# 🔐 Intrusion Detection System (IDS)  
*Hybrid IDS using Signature-based + Anomaly-based Detection*  
✨ Random Forest Classifier with 99.87% Accuracy  

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-RandomForest-green?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Accuracy-99.87%25-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/github/license/yourusername/Intrusion-detection-system" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/yourusername/Intrusion-detection-system?style=social" />
  <img src="https://img.shields.io/github/forks/yourusername/Intrusion-detection-system?style=social" />
</p>

---

## 📌 Project Overview  

This project implements a *hybrid Intrusion Detection System (IDS)* with two integrated components:  

🔹 *Signature-based detection* → Identifies *known attacks* via rule-based matching.  
🔹 *Anomaly-based detection (Random Forest)* → Detects *unknown threats* with *99.87% accuracy*.  

Both modules run *separately* but complement each other, providing *real-time monitoring dashboards* and rich visualizations.  

---

## ⚙ Features  

✔ *Signature-based packet inspection & rule alerts*  
✔ *Anomaly-based detection with Random Forest ML model*  
✔ *Real-time dashboards & visualization*  
✔ *Traffic statistics: Anomaly vs Normal*  
✔ *Easy-to-run modular design*  

---

## 🖥 Dashboards & Visualizations  

<p align="center">
  <img src="https://media.giphy.com/media/XG1oC6F9SZQk8V6lE4/giphy.gif" width="600" alt="IDS Dashboard Animation"/>
</p>

🔴 *Signature-based Intrusion Detection Logs*  
📊 *Real-Time IDS Anomaly Dashboard*  
📈 *Anomaly Detection Over Time*  
📊 *Anomaly Count vs Normal Traffic*  
⚠ *Detected Anomalies with Probability*  

---

## 📊 Model Performance  

- *Algorithm:* Random Forest Classifier 🌲  
- *Accuracy:* *99.87%*  
- *Dataset:* [Specify dataset → NSL-KDD / CICIDS]  
- *Metrics:* Precision, Recall, F1-score  

<p align="center">
  <img src="https://media.giphy.com/media/jt7bAtEijhurm/giphy.gif" width="500" alt="Model Performance Graph"/>
</p>

---

## 🚀 Installation & Usage  

```bash
# 1️⃣ Clone Repository
git clone https://github.com/yourusername/Intrusion-detection-system.git
cd intrusion-detection

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ Run Signature-based IDS
cd signature
python main.py

# 4️⃣ Run Anomaly-based IDS
cd anomaly
python detect_anomalies.py 
