import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset.csv")

print("Original Dataset:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("\nCleaned Dataset:")
print(df)

# Separate input features (X) and target (y)
X = df.drop("risk", axis=1)
y = df["risk"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))

print("\nStep 6 completed successfully!")