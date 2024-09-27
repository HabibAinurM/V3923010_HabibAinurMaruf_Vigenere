from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk enkripsi Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - ord('A')

            if char.islower():
                ciphertext += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                ciphertext += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))

            key_index += 1
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk dekripsi Vigenere Cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_len]) - ord('A')

            if char.islower():
                plaintext += chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                plaintext += chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))

            key_index += 1
        else:
            plaintext += char
    return plaintext

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        plaintext = request.form["plaintext"]
        key = request.form["key"]
        action = request.form["action"]

        if action == "Enkripsi":
            result = vigenere_encrypt(plaintext, key)
        elif action == "Dekripsi":
            result = vigenere_decrypt(plaintext, key)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
