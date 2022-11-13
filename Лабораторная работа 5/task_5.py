import random
from random import sample
def get_random_password() -> str:
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'  # TODO написать функцию генерации случайных паролей
    password = ()
    i = random.sample(alph, 8)
    password += tuple(i)
    return password
print(''.join(get_random_password()))
