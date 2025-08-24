import pandas as pd
df = pd.read_csv("KDDTrain+.txt", header=None)
print(df.iloc[:, -1].value_counts())  # Count normal vs anomaly
