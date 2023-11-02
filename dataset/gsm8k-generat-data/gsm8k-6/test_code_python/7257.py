def solution():
    beef = 20  # pounds of beef
    pork = 0.5 * beef  # pounds of pork
    total_meat = beef + pork  # total pounds of meat
    meals = total_meat / 1.5  # number of meals James can make
    total_money = meals * 20  # total amount of money James makes
    result = total_money
    return result

print(solution())