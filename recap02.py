def multiply(a: int, b: int) -> int:
    return a*b


answer = 'y'
while answer == 'y' or answer == 'Y':
    print('Give data to fill [list], (tuple), \{dictionary\}')
    input_data = input('Put some data here: ')
    print(input_data)
    answer = input('Again? [Y/n]: ')
    if not answer:
        answer = 'y'
    print()
print('Bye, bye!\n')
