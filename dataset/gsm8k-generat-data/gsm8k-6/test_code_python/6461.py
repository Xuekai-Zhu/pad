def solution():
    money = 200  # initial amount of money
    mother = (3/8) * money  # amount of money given to mother
    father = (3/10) * money  # amount of money given to father
    remaining_money = money - mother - father  # calculate remaining money
    result = remaining_money
    return result

print(solution())