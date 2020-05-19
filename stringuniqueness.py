def stringuniqueness(s):
    result = {}
    l = len(s)
    if l == 1:
        return True
    elif l == 0:
        return 0
    for i in s:
        if i in result:
            return False
        else:
            result[i] = 1
    return True
print(stringuniqueness('goo'))
print(stringuniqueness('abcdefg'))
print(stringuniqueness(''))    