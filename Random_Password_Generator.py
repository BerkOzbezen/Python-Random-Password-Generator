import random 
import string

def generate_password(length = 12):
    '''
    Generates a strong, random password of the specified length.
    It guarantees the inclusion of at least one uppercase letter, one lowercase letter,
    one digit, and one special character for better security.
    '''

    #Password must be at least 4 characters long to guarantee
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Initialize the password list with one guaranteed character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_chars = uppercase + lowercase + digits + special_chars

    # Use random.choices to select the remaining (length - 4) characters.
    # The result is a list which is concatenated (added) to the 'password' list.
    password += random.choices(all_chars , k = length - 4)

    # Shuffle the list to ensure the required characters (the first 4) are not 
    # always at the beginning, making the password structure unpredictable.
    random.shuffle(password)
    # Join the list of characters into a single string and return it.
    return ''.join(password)

try:
    user_input = input("Enter the desired password lenght (minimum 4) : ")
    # Check if the user pressed Enter (empty input).
    if user_input == "":
        # Call the function without an argument to use the default length (12).
        password = generate_password()
    else:
        # If input is not empty, attempt to convert it to an integer.
        # This is the line where ValueError will occur if the input is non-numeric (e.g., "abc").
        length = int(user_input)
        password = generate_password(length)
    print("Generated Password : ",password)
except ValueError as e:
    print(e)