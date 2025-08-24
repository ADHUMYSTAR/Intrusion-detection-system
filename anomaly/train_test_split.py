import pandas as pd
from sklearn.model_selection import train_test_split

# Load preprocessed dataset (assuming 'preprocessed.csv' is saved after preprocessing)
df = pd.read_csv("processed_data.csv")  # Change to your actual filename

# Separate features (X) and labels (y)
X = df.iloc[:, :-1]  # All columns except the last one (features)
y = df.iloc[:, -1]   # Last column (labels)

# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save train and test sets as CSV files for later use
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Dataset successfully split into training and testing sets!")
print(f"Training set size: {X_train.shape}, Testing set size: {X_test.shape}")
 