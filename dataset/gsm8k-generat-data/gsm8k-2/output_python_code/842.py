def solution():
    """Randy has $30. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. What is the amount of money, in dollars, Randy has left?"""
    initial_money = 30
    lunch_cost = 10
    remaining_money = initial_money - lunch_cost
    ice_cream_cost = remaining_money / 4
    final_money = remaining_money - ice_cream_cost
    result = final_money
    return result

print(solution())