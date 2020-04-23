# -*- coding: utf-8 -*-

def muit_tab():
    """9x9 table"""
    x = 9

    while x >= 1:
        y = 1

        while y <= x:
            '''
            In python 2, use ',' to cancle auto_change_line of print
            In python 3, use 'end=""' to cancle auto_change_line of print
            '''
            print ("%d * %d = %d\t" % (x, y, x * y)),
            y += 1
        '''change line'''
        print ""
        x -= 1


def sum_2_num(x, y):
    """
    sum two number
    :param x: number 1
    :param y: number 2
    :return: sum result
    """
    result = x + y
    return result


def print_line(char, times):
    """
    repeat print words int serviour times
    :param char: the words
    :param times: repeat times
    """
    print (char * times)

def print_lines(char, times, lines):
    """
    repeat lines
    :param char: the words
    :param times: repeat times
    :param lines: repeat line times
    """
    while lines > 0:
        print_line(char, times)
        lines -= 1

print_lines("*", 5, 3)


# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         print ("*"),
#         col += 1
#     print ""
#     row += 1



# # 1.enter the price
# price = float(input('pri/kg:'))
#
# # 2.enter the weight
# weight = float(input('kg:'))
#
# # 3.cal the final price
# def cal(price_str, weight_str):
#     a = price_str * weight_str
#     print 'price:' + str(a)
#
# cal(price, weight)



# def team(name, gender, age = 18, city = 'Tokyo'):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age', age
#     print 'city', city
#
# team('Yamata', 'Male', city='Osaka')
