# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
keys = ['bin', 'dec', 'hex', 'oct']

list_dict = [{keys[0]: bin(i), keys[1]: (i), keys[2]: hex(i), keys[3]: oct(i)} for i in range(16)]
pprint(list_dict)
