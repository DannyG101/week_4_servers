def caesar_encrypt(text, offset):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encrypted = ""
    for letter in text.lower():
        if letter == " ":
            encrypted += letter
        else:
            encrypted += letters[(letters.index(letter) + offset) % 26]
    return encrypted

def caesar_decrypt(text, offset):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encrypted = ""
    for letter in text.lower():
        if letter == " ":
            encrypted += letter
        else:
            encrypted += letters[(letters.index(letter) - offset) % 26]
    return encrypted