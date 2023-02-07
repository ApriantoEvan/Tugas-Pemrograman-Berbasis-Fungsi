from functools import reduce

def encrypt(char):
    ascii_value = ord(char)
    first_value = (ascii_value // 26) + 80
    second_value = (ascii_value % 26) + 80
    third_value = '+' if first_value > second_value else '-'
    return chr(first_value) + chr(second_value) + third_value

def encrypt_password(password):
    return reduce(lambda acc, char: acc + encrypt(char), password, '')

password = input("Enter a password (up to 100 characters): ")
encrypted_password = encrypt_password(password)
print("Encrypted password:", encrypted_password)
