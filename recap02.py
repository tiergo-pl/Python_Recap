
from operator import lshift


default_filename = 'a.txt'


def read_text_from_file(filename):
    ans = input('Put filename. If empty use default filename: ')
    if ans:
        filename = ans
    file = open(filename, 'r')
    file_contents = file.read()
    return file_contents


def string_to_list(string):
    string = string.replace("\n", " ")
    out = string.split(' ')
    return out


def string_to_tuple(string):
    string = string.replace("\n", " ")
    out = tuple(string.split(' '))
    return out


def string_to_dict(string):
    string = string.replace("\n", " ")
    out = string.split(' ')
    count_list = []
    count = 0
    for element in out:
        count_list.extend(str(count))
        count = count+1
    out2=dict(zip(count_list,out))
    return out2


answer = 'y'
while answer == 'y' or answer == 'Y':
    text_data = read_text_from_file(default_filename)
    print(text_data)
    print('Convert text into:')
    print('List:')
    input_data = string_to_list(text_data)
    print(f"input_data= {input_data}")
    print('Tuple:')
    input_data = string_to_tuple(text_data)
    print(f"input_data= {input_data}")
    print('Dict:')
    input_data = string_to_dict(text_data)
    print(f"input_data= {input_data}")

    answer = input('Again? [Y/n]: ')
    if not answer:
        answer = 'y'
    print()
print('Bye, bye!\n')
