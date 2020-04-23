
def char2num(s):
    """numbers in 0~9"""
    return {'0': 0, '1': 1, '2': 2, '3': 3, \
            '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    # def fn(x, y):
    #     """x * 10 + y"""
    #     return x * 10 + y
    # return reduce(fn, map(char2num, s))
    return  reduce(lambda x, y: x * 10 + y, map(char2num, s))

print str2int("155")