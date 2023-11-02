def solution():
    cost_of_flour = 5
    cost_of_cake_stand = 28
    money_given = 20 + 20 + 3
    total_cost = cost_of_flour + cost_of_cake_stand
    change_owed = money_given - total_cost
    result = change_owed
    return result

print(solution())