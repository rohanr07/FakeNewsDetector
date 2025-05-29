# **📰 Fake News Detector**

> An AI-powered web tool to help users determine the credibility of news articles using language models, real-time source verification, and public trust datasets.
> 

---

## **🌍 Overview**

In an age of viral misinformation, users often struggle to verify whether what they’re reading is trustworthy. This project empowers the general public with a free, intuitive, and AI-enhanced tool to check whether a given article or headline is **likely fake**, **uncertain**, or **trustworthy**.

Users can enter either a **URL** or **plain text** to receive a **probabilistic score**, along with a rationale backed by:

- AI models trained on fake/real news datasets
- Real-time source cross-checks
- Domain-level credibility data (MediaBiasFactCheck)

---

## **🎯 Goals**

- Help users understand news credibility with transparency
- Combine ML + public trust data for more robust fake news detection
- Showcase both product management and software engineering capabilities
- Demonstrate end-to-end ownership of design, development, and documentation

---

## **✨ Key Features**

| **Feature** | **Description** |
| --- | --- |
| 🔎 Text/URL Input | Paste a news snippet or URL to check |
| 📊 Scoring System | Outputs a percentage score and category (Likely Fake / Unclear / Real) |
| 🧠 ML Explanation | Shows why a piece was classified a certain way |
| 🔁 Feedback Option | Users can upvote/downvote results or report inaccuracies |
| 📈 Trending Topics | Auto-generated list of top queried news items |
| 🧾 Anonymous Usage | No login needed; optional email for feedback |

---

## **⚙️ Tech Stack**

| **Area** | **Tool/Framework** |
| --- | --- |
| Frontend | React (Vite or Next.js), CSS |
| Backend | FastAPI |
| ML Model | bert-tiny-finetuned-fake-news-detection (via HuggingFace) |
| Data APIs | NewsAPI, MediaBiasFactCheck |
| Deployment | Vercel (Frontend), Render (Backend) |
| IDE | Visual Studio Code (Mac + Win) |

---

## **📖 Documentation**

🧠 Full PM + Engineering Notion Docs:

- [Product Overview](https://www.notion.so/Reamde-md-1fa1a6d004e8801b8855d6f68c8004a6?pvs=21)
- [Functional Specs](https://www.notion.so/Reamde-md-1fa1a6d004e8801b8855d6f68c8004a6?pvs=21)
- [Scoring System](https://www.notion.so/Reamde-md-1fa1a6d004e8801b8855d6f68c8004a6?pvs=21)
- [Model & Dataset Plan](https://www.notion.so/Reamde-md-1fa1a6d004e8801b8855d6f68c8004a6?pvs=21)
- [Testing Strategy](https://www.notion.so/Reamde-md-1fa1a6d004e8801b8855d6f68c8004a6?pvs=21)

---

## **💡 Training Data

- Bulk evaluation now supports multiprocessing for rapid batch scoring across 45K+ samples
- Used True.csv and Fake.csv from Kaggle

---

## **📬 Contact & Socials**

- [GitHub](https://github.com/rohanr07)
- [LinkedIn](https://www.linkedin.com/in/rohanrenganathan/)
- [Website](https://v0-rohan-website.vercel.app)
- [Blog](https://rq7.hashnode.dev)

---

> ⚠️ Disclaimer: This tool does not perform formal fact checking and should not be used as a sole source for news decisions. Please refer to trusted outlets for final judgment.
>
