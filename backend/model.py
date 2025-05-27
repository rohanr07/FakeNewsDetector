import time
from transformers import pipeline

# loading model once
fake_news_classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection")

# labeling mappings
label_map = {
    "LABEL_0": "REAL",
    "LABEL_1": "FAKE"
}


# Function to analyze text using the BERT model with retry logic
def analyze_text(text: str, retries: int = 3, delay: float = 1.0):
    """
    Classifies text using the BERT model with retry logic.

    Parameters:
    - text: input string
    - retries: number of retry attempts if model fails
    - delay: wait time between retries in seconds
    """
    for attempt in range(retries):
        try:
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

        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise RuntimeError(f"Model failed after {retries} attempts: {str(e)}")