ALFABET_RO = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
N = len(ALFABET_RO) # 31 litere

char_to_index = {}

for index, char in enumerate(ALFABET_RO):
    char_to_index[char] = index

#p e valoarea literei din textul clar, k este valoarea literei din cheia de criptare, c este valoarea literei criptate

def GetPlainText():
    while True:
        plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
        if not plaintext:
            print("Plaintext cannot be empty. Please enter a valid plaintext.")
            continue

        for char in plaintext:
            if char not in ALFABET_RO:
                print(f"Invalid character '{char}' in plaintext. Please use only uppercase Romanian letters.")
                break
               
        else:
            return plaintext
    
def GetKey():
    while True:
        key = input("Enter the key: ").upper().replace(" ", "")
        if not key:
            print("Key cannot be empty. Please enter a valid key.")
            continue
        if len(key) < 7:
            print("Key must be at least 7 characters long. Please enter a valid key.")
            continue

        for char in key:
            if char not in ALFABET_RO:
                print(f"Invalid character '{char}' in key. Please use only uppercase Romanian letters.")
                break
        else:
            return key   


def encrypt():
    plainText = GetPlainText()
    key = GetKey()
    print(f"Plaintext: {plainText}")
    print(f"Key: {key}")

    result = []
    
    key_idx = 0
    for char in plainText:
        if char in char_to_index:
            p = char_to_index[char]
            k = char_to_index[key[key_idx % len(key)]]

            # C = (P + K) mod 31
            c = (p + k) % N
            result.append(ALFABET_RO[c])
            
            key_idx += 1
        else:

            result.append(char)
            
    return "".join(result)

def decrypt():
    cipherText = GetPlainText()
    key = GetKey()
    print(f"Ciphertext: {cipherText}")
    print(f"Key: {key}")

    result = []
    
    key_idx = 0
    for char in cipherText:
        if char in char_to_index:
            c = char_to_index[char]
            k = char_to_index[key[key_idx % len(key)]]

            # P = (C - K + 31) mod 31
            p = (c - k + N) % N
            result.append(ALFABET_RO[p])
            
            key_idx += 1
        else:
            result.append(char)
            
    return "".join(result)




def main():
    while True:
        print("Choose an option: \n 1. Encrypt \n 2. Decrypt \n 3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("Encrypting...")
            encryptedText = encrypt()
            print(f"Encrypted text: {encryptedText}")
        elif choice == '2':
            print("Decrypting...")
            decryptedText = decrypt()
            print(f"Decrypted text: {decryptedText}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

    


if __name__ == "__main__":
    main()

