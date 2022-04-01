def print_many_times(what, times=2, separator=' '):
    print(times * '{}{}'.format(what, separator))
    print(times * ('%s%s' % (what, separator)))

    # Only with mandatory argument - 1 positional argument


def print_args(*input_args):
    print(*input_args)


print_many_times('1')

print_many_times('dupka', 7, '____')
print(4*'cztery razy\n')
tup = ('aaa', 'bbb', 'ccc', 'ddd')
lis = list(tup)
print(*tup)
print(*lis)
print('To jest tupla {}{} {} {}'.format(*tup))
print_args('aa', 'bb', 'cc', 'dd')
