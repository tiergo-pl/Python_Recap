def print_args(*input_args):
    print(*input_args)


def f_with_additional_arguments(first, default='3', *cat, **bee):
    print('first: {}'.format(first))
    print('default: {}'.format(default))
    print()  # empty line
    print('cat: ', cat)
    print('unpacked cat: ', *cat)
    for arg in cat:
        print(arg)
    print
    print('bee: ', bee)
    print('unpacked bee: ', *bee)
    for k, v in bee.items():
        print('{} => {}'.format(k, v))


print(4*'cztery razy\n')
tup = ('aaa', 'bbb', 'ccc', 'ddd')
lis = list(tup)
print(*tup)
print(*lis)
print('To jest tupla {}{} {} {}'.format(*tup))
print_args('aa', 'bb', 'cc', 'dd')

f_with_additional_arguments('im first')
f_with_additional_arguments('im first', 'second', 'third', '4th', 5)
f_with_additional_arguments(
    'im first', 'im default', 5, 12, 33, k1=1, k2=2, k3=[3, 4, 5], key='value')
