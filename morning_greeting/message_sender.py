
def send_message(name, email, message):
    if not email:
        raise ValueError("Email Address is missing.")
    
    print(f"Sending message to {name} to this email address {email}: \b{message}.")
    return True

