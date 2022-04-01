default_filename='a.txt'

def read_text_from_file(filename):
    ans=input('Put filename. If empty use default filename: ')
    if ans:
        filename=ans
    file = open(filename,'r')
    file_contents=file.read()
    return file_contents

answer = 'y'
while answer == 'y' or answer == 'Y':
    text_data=read_text_from_file(default_filename)
    print(text_data)
    print('Give data to fill [list], (tuple), \{dictionary\}')
    input_data = input('Put some data here: ')
    print(f"input_data= {input_data}")
    answer = input('Again? [Y/n]: ')
    if not answer:
        answer = 'y'
    print()
print('Bye, bye!\n')
