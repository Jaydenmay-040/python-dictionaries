number_1 = 15


#a function with one parameter.
def fact(number_1):
    #returns 1 when parameter is = 1 or 0
    if number_1 == 1 or  number_1 == 0:
        return 1
    else:
        return number_1 * fact(number_1 - 1)


print(fact(number_1))
