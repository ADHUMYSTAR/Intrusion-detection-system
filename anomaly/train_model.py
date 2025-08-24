import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load preprocessed data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train_encoded.csv")
y_test = pd.read_csv("y_test_encoded.csv")

# Convert y values to 1D array
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
print("Training the model...")
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Print classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, "anomaly_detection_model.pkl")
print("Model saved as anomaly_detection_model.pkl")
