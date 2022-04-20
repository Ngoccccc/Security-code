from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

#inputs
plaintext = input('Plaintext..:')
pwd = input('Password..: ')
key = pad (pwd.encode(), AES.block_size)

#Encryption
print(AES.block_size)
def encrypt(plaintext):
    data_bytes=bytes(plaintext, 'utf-8')
    AES_obj=AES.new(key, AES.MODE_CTR)
    ciphertext=AES_obj.encrypt (data_bytes)
    return ciphertext, AES_obj.nonce
ciphertext,nonce = encrypt(plaintext)
print ('Ciphertext :',binascii.hexlify (ciphertext).decode('utf-8'))

#Decryption
def decrypt (ciphertext,nonce):
    AES_obj=AES.new (key, AES.MODE_CTR, nonce = nonce)
    raw_bytes = AES_obj.decrypt(ciphertext)
    return raw_bytes
plaintext = decrypt(ciphertext,nonce)
print ('Message...:',plaintext.decode ('utf-8'))

# "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
# key3 = "36f18357be4dbd77f050515c73fcf9f2"