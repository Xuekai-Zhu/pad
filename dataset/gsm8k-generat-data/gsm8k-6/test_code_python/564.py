def solution():
    # Find out how much money Ian has
    ian_money = Jessica_money / 2  

    # Find out how much money Rodney has
    rodney_money = ian_money + 35  

    # Find out how much more money Jessica has than Rodney
    difference = Jessica_money - rodney_money
    result = difference
    return result

print(solution())