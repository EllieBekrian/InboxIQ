def validate_value(value, allowed_values):
    if value is None:
        return False
    elif value not in allowed_values:
        return False
    else:
        return True


allowed_priorities = ["High", "Medium", "Low"]

result = validate_value("High", allowed_priorities)

print(result)

allowed_categories = [
    "Delivery",
    "Refund",
    "Technical Support",
    "Other"
]

allowed_sentiments = [
    "Positive",
    "Neutral",
    "Negative"
]

print(validate_value("Refund", allowed_categories))
print(validate_value("Angry", allowed_sentiments))

def validate_summary(summary):
    if not isinstance(summary, str):
        return False
    elif summary.strip() == "":
        return False
    else:
        return True

summary = "The customer needs help with a delayed order."

print(validate_summary(summary))

def validate_ai_response(data):
    allowed_priorities = ["High", "Medium", "Low"]
    allowed_categories = [
        "Delivery", "Refund", "Technical Support", "Other"
    ]
    allowed_sentiments = ["Positive", "Neutral", "Negative"]

    return (
    validate_value(data.get("priority"), allowed_priorities)
    and validate_value(data.get("category"), allowed_categories)
    and validate_value(data.get("sentiment"), allowed_sentiments)
    and validate_summary(data.get("summary"))
)


ai_data = {
    "priority": "High",
    "category": "Delivery",
    "sentiment": "Negative",
    "summary": "The customer needs help with a delayed order."
}

result = validate_ai_response(ai_data)

print("AI Response Valid:", result)

