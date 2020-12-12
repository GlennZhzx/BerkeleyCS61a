def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    if (k == 0):
        return result
    else:
        for i in range(k):
            result *= (n - i)
    return result 

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    """
    yString = str(y)
    result = 0
    for i in yString:
        result += int(i)
    return result
    """
    """
    #递归
    result = 0
    if y == 0:
        return 0
    else:
        result += y % 10
        return result + sum_digits(y // 10)
    """
    #迭代
    result = 0 
    while y > 0:
        result += y % 10
        y //= 10
    return result

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    """
    nString = str(n)
    count = 0
    for i in nString:
        if(i == '8'):
            count += 1
            if (count == 2):
                return True
        else:
            count = 0
    return False
    """
    """
    count = 0
    while n > 0:
        if n % 10 == 8:
            count += 1
        else:
            count = 0
        if count == 2:
            return True
        n //= 10
    return False
    """
    count = 0
    while n > 0:
        if n % 10 == 8 and count == 1:
            return True
        elif n % 10 == 8:
            count = 1
        else:
            count = 0
        n //= 10
    return False

def positive(n):
    """
    只有为0才是false
    """
    while n:
        print("positive")
        n -= 3

def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')

def bake(cake, make):
    if cake == 0:
        cake += 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make

