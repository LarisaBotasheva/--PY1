import random
import string
from random import sample
def get_random_password() -> str:
    alph = string.ascii_letters + string.digits  # TODO написать функцию генерации случайных паролей
    password = ()
    i = random.sample(alph, 8)
    password += tuple(i)
    return password
print(''.join(get_random_password()))
