from transformers import pipeline

# Load model only once
fake_news_classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")

# Map model labels to human-readable strings
label_map = {
    "LABEL_0": "REAL",
    "LABEL_1": "FAKE"
}

def analyze_text(text: str):
    result = fake_news_classifier(text)[0]
    label = result["label"]
    score = round(result["score"] * 100, 2)
    readable_label = label_map.get(label, label)
    
    message = f"The statement is likely {readable_label} with {score}% confidence."
    
    return {
        "score": score,
        "label": readable_label,
        "message": message
    }