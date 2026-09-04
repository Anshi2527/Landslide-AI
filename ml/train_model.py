import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("dataset.csv")

# Remove duplicates and missing values
df = df.drop_duplicates()
df = df.dropna()

# Input features
X = df.drop("risk", axis=1)

# Target
y = df["risk"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Create model folder
import os
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/landslide_model.pkl")

print("\n================================")
print("MODEL TRAINED SUCCESSFULLY!")
print("Model saved at:")
print("model/landslide_model.pkl")
print("================================")