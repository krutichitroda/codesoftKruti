import random
import string

def generate_password(length):
    if length < 1:
        print("Error: Password length must be at least 1 character.")
        return ""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "_main_":
    try:
        length = int(input("Enter Password Length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for password length.")