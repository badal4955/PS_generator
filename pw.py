import random
import string

def generate_password(length):
    # Define the character set to generate the password from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to Password Generator")
    print("-----------------------------")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Length must be greater than zero.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
