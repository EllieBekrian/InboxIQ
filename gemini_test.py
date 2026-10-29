import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Step 2: Create Gemini client
client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000,
        retry_options=types.HttpRetryOptions(
            attempts=1
        )
    )
)

# Step 3: Send customer email to Gemini
try:
    
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="""
Analyse this customer email:

My keyboard arrived yesterday, but some keys are not working.
Could you please help me fix this issue?

Return exactly four fields:
category, priority, sentiment, summary.

Allowed categories: Delivery, Refund, Technical Support, Other.
Allowed priorities: High, Medium, Low.
Allowed sentiments: Positive, Neutral, Negative.

Return only a valid JSON object.
"""
    )

    print("Gemini response:")
    print(response.text)

except Exception as error:
    print("Unable to get a response from Gemini.")
    print("Error type:", type(error).__name__)

print("Program finished.")