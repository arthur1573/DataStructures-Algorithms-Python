


####################### Call stack

def funcThree():
    print('Three')


def funcTwo():
    funcThree()
    print('Two')


def funcOne():
    funcTwo()
    print('One')

funcOne()











################ print factorial number in human way


n = 4
print(str(n) + "! = ", end = '')
def factorial(n):
    '''
    print factorial number in human way
    '''
    if n < 0:
        return 'factorial() not defined for negative values'
    if n == 0:
        return 1
    if n == 1:
        print('', n, '= ', end = '')
        return 1
    else:
        print('', n, '*', end = '')
        return n * factorial(n - 1)


print(factorial(n))




