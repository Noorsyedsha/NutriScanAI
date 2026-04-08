# 🍎 NutriScan AI: Agentic Personalized Nutritionist
**Built for Gen AI Academy APAC Edition**

NutriScan AI is a high-impact, agentic health-tech solution that bridges the gap between wearable biometric data and real-time dietary choices. Using the **Agent Development Kit (ADK)** and **Gemini 1.5 Flash**, it provides hyper-personalized food safety verdicts based on a user's live physiological state.

---

## 🚀 Problem Statement
Traditional nutrition labels provide static data that doesn't account for individual health conditions. For a diabetic or hypertensive user, a "standard" snack can be dangerous depending on their current blood sugar or heart rate. NutriScan AI provides the missing context to prevent adverse health events.

## 🛠️ Tech Stack & Google Services
* **Orchestration:** Agent Development Kit (ADK) for multi-agent reasoning.
* **AI Brain:** Gemini 1.5 Flash (Vertex AI) for multimodal food label analysis.
* **Vector Database:** AlloyDB AI for storing and retrieving long-term health trends and user profiles.
* **Compute:** Google Cloud Run (Serverless).
* **Connectivity:** Model Context Protocol (MCP) for secure biometric data ingestion.

---

## 🧠 Agentic Workflow

1.  **Biometric Agent (Researcher):** Retrieves real-time metrics (Glucose, HR) and historical health context from **AlloyDB AI**.
2.  **Vision Agent (Analyst):** Performs multimodal OCR on the food item/label to extract nutritional facts (Sugar, Sodium, Allergens).
3.  **Nutritionist Agent (The Decider):** An **ADK-managed agent** that synthesizes data from both agents to provide a Green/Yellow/Red verdict with clinical reasoning.

---

## ✨ Key Features
* **Multimodal Input:** Analyze food via photos or live video streams.
* **Personalized Guardrails:** Custom safety thresholds for Diabetes, Hypertension, and Allergies.
* **Predictive Alerts:** Foresees potential glucose spikes based on historical data in AlloyDB AI.
* **Closed-Loop Feedback:** Learns from user reactions to improve future recommendations.

---

## ⚙️ Installation & Setup

### 1. Enable GCP Services
```bash
gcloud services enable aiplatform.googleapis.com alloydb.googleapis.com run.googleapis.com
