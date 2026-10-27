from email_utils import analyse_email
def test_word_count():
    assert analyse_email("Hello") == (1, 5)
    
    
def test_two_words():
    assert analyse_email("order delayed")==(2,13)
    
def test_empty_email():
    assert analyse_email("")==(0,0)
    
def test_whitespace_email():
    assert analyse_email("   ")==(0,3)