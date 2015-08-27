from random import SystemRandom
from string import ascii_lowercase, digits


def generate_username(length=8):
    return ''.join(SystemRandom().choice(ascii_lowercase) for _ in range(length)

def generate_password(length=8):
    return ''.join(SystemRandom().choice(ascii_lowercase + digits) for _ in range(length))
