import random
from random import sample
def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    list_len = 15
    i = random.sample(range(-10, 11), 15)
    list_numbers.append(i)
    return list_numbers
print(get_unique_list_numbers())
