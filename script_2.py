

print('''
{0:<5} {0:08b}
{1:<5} {1:08b}
'''.format(2, 255))



list1 = '1 2 3 4'
e1, e2, e3, e4 = list1.split()
print('{} {} {} {}'.format(e1, e2, e3, e4))


template = '{:2}'*4
print(template.format(e1, e2, e3, e4))

if a < 5:
    print('a меньше 5')
    print('-'*10)
else:
    print('a больше или равно 5')
    print('='*10)