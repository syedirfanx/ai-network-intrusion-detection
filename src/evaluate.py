from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import os

def evaluate(y_test, preds):
    os.makedirs("results", exist_ok=True)

    report = classification_report(y_test, preds)

    with open("results/classification_report.txt", "w") as f:
        f.write(report)

    cm = confusion_matrix(y_test, preds)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig("results/confusion_matrix.png")