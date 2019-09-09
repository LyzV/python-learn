

def adder(*nums: int) -> str:
    """Calculate sum of all in nums"""
    s = 0
    for n in nums:
        s += n
    print("Sum: ", s)
    return s


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)


def info(**data) -> None:
    """Print info key:value"""
    print("\nData type of argument: ", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


info(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
info(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

print('\n' + adder.__doc__)
print(info.__doc__)
