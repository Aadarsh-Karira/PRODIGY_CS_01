def encryption(plaintext, key):
    cipher_text = ""
    for char in plaintext:
        if char.isupper():
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            cipher_text += char
    print("Encrypted Text is:", cipher_text)

def decryption(cipher_text, key):
    plaintext = ""
    for char in cipher_text:
        if char.isupper():
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        else:
            plaintext += char
    print("\nPlain Text For Your CipherText is:", plaintext)

def main():
    print("Press 1 for Encryption")
    print("Press 2 for Decryption")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        text = input("Enter Text for Encryption: ")
        key = int(input("Enter Key: "))
        encryption(text, key)
    elif choice == 2:
        text = input("Enter Encrypted Text to Decrypt: ")
        key = int(input("Enter Key: "))
        decryption(text, key)
    else:
       print("EXITED THE PROGRAM.THANKYOU!")

if __name__ == "__main__":
    main()
