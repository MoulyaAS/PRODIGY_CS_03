import re
from termcolor import colored  # For color-coded feedback, install using 'pip install termcolor'

# Function to evaluate password strength
def evaluate_password_strength(password):
    # Initialize the strength score
    strength_score = 0
    
    # Set of criteria to check for
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    # Check if the password meets each criterion
    for key, met in criteria.items():
        if met:
            strength_score += 1
    
    # Provide feedback based on the strength score
    feedback = []
    if strength_score == 5:
        feedback.append(colored("Your password is strong.", "green"))
    elif 3 <= strength_score < 5:
        feedback.append(colored("Your password is moderate.", "yellow"))
        feedback.append(colored("Suggestions to improve password strength:", "yellow"))
    else:
        feedback.append(colored("Your password is weak.", "red"))
        feedback.append(colored("Suggestions to improve password strength:", "red"))
    
    # Give feedback on missing criteria
    if not criteria["length"]:
        feedback.append("- Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("- Include at least one uppercase letter (A-Z).")
    if not criteria["lowercase"]:
        feedback.append("- Include at least one lowercase letter (a-z).")
    if not criteria["digit"]:
        feedback.append("- Include at least one number (0-9).")
    if not criteria["special_char"]:
        feedback.append("- Include at least one special character (!@#$%^&*(), etc.).")
    
    return feedback, strength_score

# Main function to interact with the user
def main():
    print("Password Strength Checker Tool")
    
    while True:
        password = input("\nEnter a password to check its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            print("Exiting the tool.")
            break
        
        # Evaluate password strength
        feedback, score = evaluate_password_strength(password)
        
        # Print feedback
        print("\nPassword Strength Feedback:")
        for line in feedback:
            print(line)
        
        # Display the strength score
        print(colored(f"\nStrength Score: {score}/5\n", "cyan"))

# Run the program
if __name__ == "__main__":
    main()
