def palindrome(text):
    text = text.replace(" ", "").lower()
    
    if not text:
        return False
    
    return text == text[::-1]

def main():
    user_input = input("Enter a text: ")
    
    if palindrome(user_input):
        print('True')
    else:
        print('False')

if __name__ == "__main__":
    main()

