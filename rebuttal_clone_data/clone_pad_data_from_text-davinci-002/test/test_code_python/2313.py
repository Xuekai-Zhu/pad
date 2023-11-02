def solution():
    money_given = 47
    cost_of_bread = 2
    cost_of_milk = 2
    bread_bought = 4
    milk_bought = 2
    total_spent = cost_of_bread * bread_bought + cost_of_milk * milk_bought
    money_left = money_given - total_spent
    result = money_left
    return result

print(solution())