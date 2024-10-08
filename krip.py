def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Contoh penggunaan
if __name__ == "__main__":
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan jumlah pergeseran (0-25): "))
    
    encrypted = caesar_encrypt(text, shift)
    print("Teks terenkripsi:", encrypted)
    
    decrypted = caesar_decrypt(encrypted, shift)
    print("Teks terdekripsi:", decrypted)