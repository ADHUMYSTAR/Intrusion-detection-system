🔐 Intrusion Detection System (IDS)

Hybrid IDS using Signature-based + Anomaly-based Detection (Random Forest Classifier with 99.87% Accuracy)

📌 Project Overview

This project implements a hybrid Intrusion Detection System (IDS) with two components:

Signature-based detection → Identifies known attacks using rule-based matching.

Anomaly-based detection (Random Forest Classifier) → Detects unknown threats with 99.87% accuracy.

Both modules run separately and provide real-time monitoring dashboards.

⚙️ Features

✔️ Signature-based packet inspection & rule alerts
✔️ Anomaly-based detection using Random Forest ML model
✔️ Real-time visualization dashboards
✔️ Anomaly vs Normal traffic statistics
✔️ Easy-to-run modular design

📂 Project Structure
├── anomaly/              # ML-based anomaly detection module
│   ├── train_model.py    # Train Random Forest model
│   ├── dashboard.py      # Real-time anomaly detection dashboard
│   └── ...  
│
├── signature/            # Signature-based detection module
│   ├── rules/            # Detection rules
│   ├── sniffer.py        # Packet sniffer and rule matcher
│   └── dashboard.py      # Real-time signature logs dashboard
│
├── datasets/             # Dataset used for training/testing
├── models/               # Saved ML models
├── requirements.txt      # Dependencies
└── README.md             # Documentation

🖥️ Dashboards & Visualizations
🔴 Signature-based Intrusion Detection Logs
<img width="1558" height="883" alt="image" src="https://github.com/user-attachments/assets/48b4c108-a899-474b-9ea0-92a9dd00c7d4" />


📊 Real-Time IDS Anomaly Dashboard
<img width="671" height="528" alt="image" src="https://github.com/user-attachments/assets/546722b0-3c54-4521-979f-a4593a068436" />

📈 Anomaly Detection Over Time
<img width="692" height="320" alt="image" src="https://github.com/user-attachments/assets/2597968c-28a7-496b-bf74-d423a2304f59" />

📊 Anomaly Count vs Normal Traffic
<img width="738" height="520" alt="image" src="https://github.com/user-attachments/assets/9b5569c9-df28-49d8-bebb-6bf883c765df" />

⚠️ Detected Anomalies with Probability
<img width="704" height="471" alt="image" src="https://github.com/user-attachments/assets/482b865c-f4a8-4631-b1d5-ef8148356709" />

📊 Model Performance

Algorithm: Random Forest Classifier

Accuracy: 99.87%

Dataset: [Specify dataset, e.g., NSL-KDD / CICIDS]

Metrics: Precision, Recall, F1-score

🚀 Installation & Usage
1️⃣ Clone Repository
git clone https://github.com/yourusername/Intrusion-detection-system.git
cd intrusion-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Signature-based IDS
cd signature
python sniffer.py

4️⃣ Run Anomaly-based IDS
cd anomaly
python dashboard.py


Dashboards will be available at:

Signature Logs → http://localhost:5000/signature

Anomaly Dashboard → http://localhost:5000/anomaly
