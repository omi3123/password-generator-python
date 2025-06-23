import random
def generate_password(length):
    password = ''
    for _ in range(length):
        password += str(random.randint(0, 9))
    return password
password_length = 8
print("Generated Password:", generate_password(password_length))