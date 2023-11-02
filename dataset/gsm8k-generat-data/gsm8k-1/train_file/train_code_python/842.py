def solution():
    """Randy has $30. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. What is the amount of money, in dollars, Randy has left?"""
    starting_money = 30
    lunch_cost = 10
    money_left = starting_money - lunch_cost
    ice_cream_cost = money_left / 4
    money_left -= ice_cream_cost
    result = money_left
    return result

print(solution())