import random

class Shuffler:
    def __init__(self):
        self.secret_number = random.randint(1, 100)

    def encrypt(self, number):
        operation = random.choice([1, -1])
        result = number + operation * self.secret_number
        return result

    def decrypt(self, encrypted_number):
        operation = 1 if encrypted_number > self.secret_number else -1
        result = encrypted_number + operation * self.secret_number
        return result

shuffler = Shuffler()

original_number = 42
encrypted_number = shuffler.encrypt(original_number)
print(f"Шифроване число: {encrypted_number}")

# Розшифровуємо число
decrypted_number = shuffler.decrypt(encrypted_number)
print(f"Розшифроване число: {decrypted_number}")
