import re

# Function to check the password strength
def check_password_strength(password):
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    
    score = sum([length, has_upper, has_lower, has_digit, has_special])

  
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    
    improvements = []
    if not length:
        improvements.append("Increase the length to at least 8 characters.")
    if not has_upper:
        improvements.append("Add at least one uppercase letter.")
    if not has_lower:
        improvements.append("Add at least one lowercase letter.")
    if not has_digit:
        improvements.append("Add at least one number.")
    if not has_special:
        improvements.append("Add at least one special character (!@#$%^&* etc.).")


    print(f"Password Strength: {strength}")
    if improvements:
        print("Suggestions for improvement:")
        for suggestion in improvements:
            print(f"- {suggestion}")


password = input("Enter your password: ")
check_password_strength(password)