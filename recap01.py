def multiply(a: int, b: int) -> int:
    return a*b


answer = 'y'
while answer == 'y' or answer == 'Y':
    print('Give two numbers:\nx= ', end='')
    x = int(input())
    #print('y= ', end='')
    y = int(input('y= '))
    print('x * y =', multiply(x, y))
    answer = input('Again? [Y/n]: ')
    if not answer:
        answer = 'y'
    print()
print('Bye, bye!\n')
