def print_many_times(what, times=2, separator=' '):
    print(times * '{}{}'.format(what, separator))
    print(times * ('%s%s' % (what, separator)))

    # Only with mandatory argument - 1 positional argument



print_many_times('1')

print_many_times('dupka', 7, '____')
