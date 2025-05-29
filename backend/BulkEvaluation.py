import pandas as pd
from sklearn.metrics import classification_report
from tqdm import tqdm
from multiprocessing import Pool, cpu_count, freeze_support
from transformers import pipeline
import time

# These will be initialized in each process
fake_news_classifier = None
label_map = None


def init_worker():
    global fake_news_classifier, label_map
    fake_news_classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")
    label_map = {
        "LABEL_0": "REAL",
        "LABEL_1": "FAKE"
    }

def process_row(data):
    text, true_label = data
    try:
        result = fake_news_classifier(text)[0]
        label = result["label"]
        score = round(result["score"] * 100, 2)
        readable_label = label_map.get(label, label)
        predicted_label = 1 if readable_label == "FAKE" else 0

        if predicted_label != true_label:
            print(f"❌ Misclassified: {text[:80]}... -> predicted: {predicted_label}, true: {true_label}")

        return {
            "text": text,
            "true_label": true_label,
            "predicted_label": predicted_label,
            "score": score,
            "message": f"The statement is likely {readable_label} with {score}% confidence."
        }

    except Exception as e:
        return {
            "text": text,
            "true_label": true_label,
            "predicted_label": None,
            "error": str(e)
        }


def main():
    print(f"🚀 Using {cpu_count()} cores...")

    fake_df = pd.read_csv("backend/data/Fake.csv")
    true_df = pd.read_csv("backend/data/True.csv")

    fake_df["label"] = 1
    true_df["label"] = 0

    df = pd.concat([fake_df, true_df], ignore_index=True)
    df = df[["text", "label"]].dropna()

    # Convert to list of tuples (text, label) for safe pickling
    data = list(zip(df["text"], df["label"]))

    with Pool(cpu_count(), initializer=init_worker) as pool:
        predictions = list(tqdm(pool.imap(process_row, data), total=len(data)))

    results_df = pd.DataFrame(predictions)
    valid = results_df.dropna(subset=["predicted_label"])

    y_true = valid["true_label"]
    y_pred = valid["predicted_label"]
    print("Classification Report:\n")
    print(classification_report(y_true, y_pred, target_names=["REAL", "FAKE"]))

    results_df.to_csv("evaluation_results.csv", index=False)
    misclassified = valid[valid["true_label"] != valid["predicted_label"]]
    misclassified.to_csv("misclassified_samples.csv", index=False)


if __name__ == "__main__":
    freeze_support()
    main()