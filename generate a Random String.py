import random
import string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

string_length = 8

result = generate_random_string(string_length)

print("Generated Random String:", result)
