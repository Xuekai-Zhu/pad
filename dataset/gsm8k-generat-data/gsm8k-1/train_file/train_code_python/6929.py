def solution():
    """Josh has 9 dollars. He spent $1.75 on a drink, and then spent another $1.25. How much money, in dollars, does Josh have left?"""
    initial_money = 9
    drink_cost = 1.75
    second_cost = 1.25
    remaining_money = initial_money - drink_cost - second_cost
    result = remaining_money
    return result

print(solution())