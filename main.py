def is_palindrome(text):
    # Removing white spaces and converting to lowercase
    text = text.replace(" ", "").lower()
    
    # Checking if the text is empty
    if not text:
        return False
    
    # Checking if the text is a palindrome
    return text == text[::-1]

def main():
    # Getting input from the user
    user_input = input("Enter a text: ")
    
    # Checking if the input is a palindrome
    if is_palindrome(user_input):
        print('True')
    else:
        print('False')

if __name__ == "__main__":
    main()

