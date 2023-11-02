def solution():
    cost_of_pizza = 12
    cost_of_juice = 2
    number_of_pizza = 2
    number_of_juice = 2
    total_cost = (cost_of_pizza * number_of_pizza) + (cost_of_juice * number_of_juice)
    money_given = 50
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())