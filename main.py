from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import json
from caesar_encryption_functions import caesar_encrypt, caesar_decrypt

class EncryptionBody(BaseModel):
    text : str
    offset : int
    mode : str

class DecryptionBody(BaseModel):
    text : str

app = FastAPI()


@app.get("/test/")
def test():
    return {"msg":"hi from test"}


@app.get("/test/{name}")
def save_name(name:str):
    with open("names.txt", "a") as f:
        f.write(f"\n{name}")
    return {"msg":"saved user"}

@app.post("/caesar")
def caesar_encrypt_or_decrypt(word:EncryptionBody):
    if word.mode == "encrypt":
        encrypted = caesar_encrypt(word.text, word.offset)
        return {"encrypted text" : encrypted}
    else:
        decrypted = caesar_decrypt(word.text, word.offset)
        return {"encrypted text": decrypted}

@app.get("/fence/encrypt/")
def fence_encrypt(text : str):
    word = text.replace(" ", "")
    first = ""
    second = ""
    for i in range(len(word)):
        if i % 2 == 0:
            first += word[i]
        else:
            second += word[i]
    encrypted = first + second
    return {"encrypted_text" : encrypted}

@app.post("/fence/decrypt/")
def fence_decrypt(text:DecryptionBody):
    word = text.text.replace(" ", "")
    decrypted = ""
    for i in range(len(word) // 2):
        decrypted += word[i]
        decrypted += word[(len(word) // 2) + i]
    return  {"decrypted_text" : decrypted}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


