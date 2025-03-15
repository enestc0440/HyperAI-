import hashlib

class QuantumEncryptor:
    def __init__(self, key_length=128):
        self.key = hashlib.sha256(str(key_length).encode()).hexdigest()

    def encrypt(self, data):
        encrypted = hashlib.sha256(data.encode()).hexdigest()
        return f"Şifrelenmiş Veri: {encrypted}"
