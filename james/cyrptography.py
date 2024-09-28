import random
import string

def key(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + ' '
    return ''.join(random.choice(chars)
                    for _ in range(size))

def position(char):
    if char == ' ':
        return 52  
    elif char.isupper():  
        return ord(char) - ord('A')
    elif char.islower():  
        return ord(char) - ord('a') + 26

def get_char(position):
    if position == 52:
        return ' '  
    elif position < 26:
        return chr(position + ord('A'))  
    else:
        return chr(position - 26 + ord('a'))  

def encode(message, random):
    result = ''
    for msg, key in zip(message, random):
        mpos = position(msg)
        pos = position(key)
        new = (mpos + pos) % 53  
        result += get_char(new)
    return result

def text(message, random):
    original = ''
    for char, key in zip(message, random):
        enc = position(char)
        kpos = position(key)
        orig = (enc - kpos) % 53  
        original += get_char(orig)
    return original

userinput = input("Enter the message ")

gkey = key(len(userinput))

message = encode(userinput, gkey)
print(f"Plain Text :  {userinput}")
print(f"Key:     {gkey}")
print(f"cipher text :   {message}")

decoded_message = text(message, gkey)
print(f"decrypted text :   {decoded_message}")