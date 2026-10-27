from email_utils import analyse_email, validate_ai_response
def test_word_count():
    assert analyse_email("Hello") == (1, 5)
    
    
def test_two_words():
    assert analyse_email("order delayed")==(2,13)
    
def test_empty_email():
    assert analyse_email("")==(0,0)
    
def test_whitespace_email():
    assert analyse_email("   ")==(0,3)
    
def test_valid_ai_response():
    ai_data = {
        "priority": "High",
        "category": "Delivery",
        "sentiment": "Negative",
        "summary": "The customer reports a delayed order."
    }

    assert validate_ai_response(ai_data) is True
    
def test_invalid_ai_response():
    ai_data = {
        "priority": "High",
        "category": "Delivery",
        "sentiment": "Angry",
        "summary": "The customer reports a delayed order."
    }

    assert validate_ai_response(ai_data) is False
    
def test_missing_priority():
    ai_data = {
        "category": "Delivery",
        "sentiment": "Negative",
        "summary": "The customer reports a delayed order."
    }

    assert validate_ai_response(ai_data) is False
    
def test_empty_summary():
    ai_data = {
        "priority": "High",
        "category": "Delivery",
        "sentiment": "Negative",
        "summary": "   "
    }

    assert validate_ai_response(ai_data) is False