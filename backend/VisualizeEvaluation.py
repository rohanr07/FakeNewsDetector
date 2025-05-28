import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix

df = pd.read_csv("evaluation_results.csv")
valid = df.dropna(subset=["predicted_label"])

y_true = valid["true_label"]
y_pred = valid["predicted_label"]

# Plot Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=["REAL", "FAKE"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# Optional: Bar chart of class distribution
valid["predicted_label"].value_counts().plot(kind="bar", title="Predicted Label Distribution")
plt.xlabel("Label")
plt.ylabel("Count")
plt.show()