def filter_len_str_more_4(string):
    if len(string) >= 5:
        return True
    else:
        return False


def filter_len_str_even(string):
    if (len(string) % 2) == 0:
        return True
    else:
        return False


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = list(map(len, filter(filter_len_str_more_4, first_strings)))
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
even_string = list(filter(filter_len_str_even, first_strings)) + list(filter(filter_len_str_even, second_strings))
third_result = {f'{i}': len(i) for i in even_string}

print(first_result)
print(second_result)
print(third_result)
