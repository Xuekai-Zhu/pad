def solution():
    twenties = 2
    fives = 3
    loose_change = 4.50
    cost_of_cake = 17.50
    total_money = twenties * 20 + fives * 5 + loose_change
    money_left = total_money - cost_of_cake
    result = money_left
    return result

print(solution())