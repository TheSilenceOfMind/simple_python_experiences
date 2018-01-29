def summarise(a, b):
    """This func summarize two numbers"""
    try:
        s = a + b
        return int(s)
    except:
        return 'error'


def get_num(prompt):
    """get num form user and return entered number"""
    str = input(prompt)
    try:
        num = int(str)
    except:
        pass
    else:
        return num


while True :
    a = get_num('enter 1 num: ')
    if a:
        break
while True:
    b = get_num('enter 2 num: ')
    if b:
        break
print(str(a) + ' + ' + str(b) + ' = ' + str(summarise(a, b)))