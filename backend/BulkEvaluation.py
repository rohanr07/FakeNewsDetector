import pandas as pd
from model import analyze_text
from sklearn.metrics import classification_report, confusion_matrix
from tqdm import tqdm

import json

# loading datasets
fake_df = pd.read_csv("backend/data/Fake.csv")
true_df = pd.read_csv("backend/data/True.csv")

# adding label column (1 for fake, 0 for real)
fake_df["label"] = 1
true_df["label"] = 0

# combining the 2 datasets
df = pd.concat([fake_df, true_df], ignore_index=True)

# using only text and label columns from the dataset
df = df[["text", "label"]].dropna()


predictions = []
for row in tqdm(df.itertuples(index=False), total=len(df)):
    try:
        result = analyze_text(row.text)
        predicted_label = 1 if result["label"] == "FAKE" else 0

        if predicted_label != row.label:
            print(f"❌ Misclassified: {row.text[:80]}... -> predicted: {predicted_label}, true: {row.label}")

        predictions.append({
            "text": row.text,
            "true_label": row.label,
            "predicted_label": predicted_label,
            "score": result["score"],
            "message": result["message"]
        })
    except Exception as e:
        predictions.append({
            "text": row.text,
            "true_label": row.label,
            "predicted_label": None,
            "error": str(e)
        })


# creating DataFrame from predictions
results_df = pd.DataFrame(predictions)

# filtering only successful predictions
valid = results_df.dropna(subset=["predicted_label"])

# printing metrics
y_true = valid["true_label"]
y_pred = valid["predicted_label"]
print("Classification Report:\n")
print(classification_report(y_true, y_pred, target_names=["REAL", "FAKE"]))

# save full results
results_df.to_csv("evaluation_results.csv", index=False)

misclassified = valid[valid["true_label"] != valid["predicted_label"]]
misclassified.to_csv("misclassified_samples.csv", index=False)