def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char  # Leave non-alphabetic characters unchanged

    return result

def decrypt(text, key):
    return encrypt(text, -key)  # Decryption is just encryption with negative shift

def main():
    print("\n=== Caesar Cipher Tool ===")
    
    while True:
        choice = input("\nDo you want to (E)ncrypt or (D)ecrypt a message? (E/D, or Q to quit): ").upper()
        
        if choice == 'Q':
            print("\nGoodbye!\n")
            break
        elif choice not in ('E', 'D'):
            print("\nInvalid choice. Please enter E, D, or Q.")
            continue

        message = input("\nEnter your message: ")
        try:
            key = int(input("\nEnter shift value (number): "))
        except ValueError:
            print("\nShift must be an integer.")
            continue

        if choice == 'E':
            result = encrypt(message, key)
            print("\nEncrypted message:", result)
        else:
            result = decrypt(message, key)
            print("\nDecrypted message:", result)

        print()

if __name__ == "__main__":
    main()
