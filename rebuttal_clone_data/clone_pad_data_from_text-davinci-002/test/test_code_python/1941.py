def solution():
    money_given = 74
    cost_of_bread = 5
    cost_of_orange_juice = 2
    number_of_items_bought = 9
    total_cost = cost_of_bread * 5 + cost_of_orange_juice * 4
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())