def get_count_char(str_):# TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.lower())
    dict_ = {}
    for letter in str_:
        if letter.isalpha():
            if letter not in dict_:
                dict_[letter] = 1
            else:
                dict_[letter] += 1
    return(dict_)
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))


def percent_count_car(str_two):
    str_ = "".join(str_two.lower())
    dict_two = {}
    for letter in str_:
        if letter.isalpha():
            if letter not in dict_two:
                dict_two[letter] = 1
            else:
                dict_two[letter] += 1
    total = sum(dict_two.values())
    for key, val in dict_two.items():
        dict_two[key] = round(val / total * 100, 2)
    return(dict_two)

print(percent_count_car(main_str))
