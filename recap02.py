
default_filename = 'a.txt'
output_filename='out.txt'

def print_write_file(file_obj,*print_args):
    print(*print_args)
    print(*print_args, file=file_obj)


def read_text_from_file(filename):
    ans = input('Put filename. If empty use default filename: ')
    if ans:
        filename = ans
    file = open(filename, 'r')
    file_contents = file.read()
    file.close()
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
        count_list.append(str(count))
        count = count+1
    out2 = dict(zip(count_list, out))
    return out2


def string_to_dict2(string):
    string = string.replace("\n", " ")
    out = string.split(' ')
    count_list = list(range(len(out)))
    out2 = dict(zip(count_list, out))
    return out2


out_file = open(output_filename,'w')
answer = 'y'
while answer == 'y' or answer == 'Y':
    text_data = read_text_from_file(default_filename)
    print_write_file(out_file,text_data)
    print_write_file(out_file, 'Convert text into:')
    print_write_file(out_file, 'List:')
    input_data = string_to_list(text_data)
    print_write_file(out_file, f"input_data= {input_data}")
    print_write_file(out_file, 'Tuple:')
    input_data = string_to_tuple(text_data)
    print_write_file(out_file, f"input_data= {input_data}")
    print_write_file(out_file, 'Dict:')
    input_data = string_to_dict(text_data)
    print_write_file(out_file, f"input_data= {input_data}")
    print_write_file(out_file, 'Dict2:')
    input_data = string_to_dict2(text_data)
    print_write_file(out_file, f"input_data= {input_data}")

    answer = input('Again? [Y/n]: ')
    if not answer:
        answer = 'y'
    print_write_file(out_file)
out_file.close()
print('Bye, bye!\n')
