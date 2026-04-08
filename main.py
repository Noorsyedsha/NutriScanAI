import vertexai
from vertexai.generative_models import GenerativeModel, Image, Part
from fastapi import FastAPI, UploadFile, File
import json

# Initialize Vertex AI
PROJECT_ID = "your-project-id"
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

app = FastAPI()
model = GenerativeModel("gemini-1.5-flash")


# Mock function to simulate fetching data from a smartwatch/Health Connect
def get_mock_health_metrics():
    return {
        "heart_rate": 85,
        "blood_sugar": 145,  # Slightly high
        "allergies": ["peanuts", "shellfish"],
        "conditions": ["type-2 diabetes"]
    }


@app.post("/scan-food")
async def scan_food(file: UploadFile = File(...)):
    # 1. Get real-time health data
    health_context = get_mock_health_metrics()

    # 2. Prepare the Image for Gemini
    image_bytes = await file.read()
    food_image = Part.from_data(data=image_bytes, mime_type="image/jpeg")

    # 3. Formulate the "Reasoning" Prompt
    prompt = f"""
    You are a personalized health assistant. 
    Analyze the provided image of a food item or nutrition label.

    USER HEALTH CONTEXT:
    - Conditions: {health_context['conditions']}
    - Current Blood Sugar: {health_context['blood_sugar']} mg/dL
    - Allergies: {health_context['allergies']}

    TASK:
    1. Identify the food item or read the nutrition label.
    2. Determine if it is safe for this specific user to eat RIGHT NOW.
    3. Return a JSON response with:
       - "status": "Green" (Safe), "Yellow" (Caution), or "Red" (Danger)
       - "reason": A short 1-sentence explanation.
       - "nutrients_detected": Key facts like sugar or sodium content.
    """

    # 4. Generate Content
    response = model.generate_content(
        [food_image, prompt],
        generation_config={"response_mime_type": "application/json"}
    )

    return json.loads(response.text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
