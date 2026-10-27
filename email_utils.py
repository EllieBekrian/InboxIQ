def analyse_email(email_text):
    word_count = len(email_text.split())
    character_count = len(email_text)

    return word_count, character_count

def validate_value(value, allowed_values):
    if value is None:
        return False
    elif value not in allowed_values:
        return False
    else:
        return True
    
def validate_summary(summary):
    if not isinstance(summary, str):
        return False
    elif summary.strip() == "":
        return False
    else:
        return True
    
def validate_ai_response(data):
    allowed_priorities = ["High", "Medium", "Low"]

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

    return (
        validate_value(data.get("priority"), allowed_priorities)
        and validate_value(data.get("category"), allowed_categories)
        and validate_value(data.get("sentiment"), allowed_sentiments)
        and validate_summary(data.get("summary"))
    )