import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from src.preprocess import load_data, preprocess
from src.train import train_model
from src.evaluate import evaluate

# ==================================================
# 1. Setup folders
# ==================================================
os.makedirs("results", exist_ok=True)
os.makedirs("models", exist_ok=True)

# ==================================================
# 2. Load + Preprocess
# ==================================================
print("Loading dataset...")
df = load_data()

print("Preprocessing data...")
X, y = preprocess(df)

# ==================================================
# 3. Train Model
# ==================================================
print("Training model...")
model, X_test, y_test, preds, acc = train_model(X, y)

joblib.dump(model, "models/nids_model.pkl")

# ==================================================
# 4. Evaluate
# ==================================================
evaluate(y_test, preds)

prec = precision_score(y_test, preds)
rec = recall_score(y_test, preds)
f1 = f1_score(y_test, preds)

# ==================================================
# 5. Print Core Metrics
# ==================================================
print("\n" + "=" * 55)
print("MODEL PERFORMANCE")
print("=" * 55)
print(f"Accuracy : {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall   : {rec:.4f}")
print(f"F1 Score : {f1:.4f}")

# ==================================================
# 6. Confusion Matrix
# ==================================================
cm = confusion_matrix(y_test, preds)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png")
plt.close()

# ==================================================
# 7. Feature Importance
# ==================================================
importance = model.feature_importances_

feat = pd.Series(importance, index=X.columns)
feat = feat.sort_values(ascending=True).tail(10)

plt.figure(figsize=(8,5))
feat.plot(kind="barh")
plt.title("Top 10 Important Features")
plt.tight_layout()
plt.savefig("results/feature_importance.png")
plt.close()

# ==================================================
# 8. Final Summary
# ==================================================
print("\nOutputs generated successfully.")
print("Saved model: models/nids_model.pkl")
print("\nGenerated in /results folder:")
print("- confusion_matrix.png")
print("- feature_importance.png")
print("=" * 55)