
def cmp(a=5.0, b=7.1):
    if a > b:
        print('a is more then b')
    elif a < b:
        print('b is more then a')
    else:
        print('a is equal to b')


def cmp(a='one', b='two'):
    if a > b:
        print('string a is more then b one')
    elif b > a:
        print('string b is more then a one')
    else:
        print('both strings are equal')


cmp(5, 4)

first = 68
second = 92

cmp(first, second)

s1 = '13764'
s2 = '765434'
cmp(s1, s2)

print('Finish.')
