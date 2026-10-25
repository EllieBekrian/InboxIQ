# InboxIQ - AI Email Assistant

def analyse_email(email_text):
    word_count = len(email_text.split())
    character_count=len(email_text)
    
    return word_count,character_count


customer_email = input("Enter customer email: ")

word_count, character_count = analyse_email(customer_email)
print("Email word count:", word_count)
print("character count:",len(customer_email))