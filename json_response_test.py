import json
from email_utils import validate_ai_response

response_text = """
{
    "category": "Technical Support",
    "priority": "Medium",
    "sentiment": "Negative",
    "summary": "Customer received a keyboard with non-functioning keys."
}
"""

ai_data = json.loads(response_text)

print("Category:", ai_data["category"])
print("Priority:", ai_data["priority"])
print("Sentiment:", ai_data["sentiment"])

is_valid = validate_ai_response(ai_data)

print("AI Response Valid:", is_valid)