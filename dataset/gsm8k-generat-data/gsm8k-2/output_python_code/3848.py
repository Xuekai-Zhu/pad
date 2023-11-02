def solution():
    """Randy has some money. He spent $10 buying his lunch. He spent a quarter of the money he had left on an ice cream cone. If the ice cream cone cost $5, what is the amount of money, in dollars, Randy had at first?"""
    lunch_cost = 10
    ice_cream_cost = 5
    remaining_money = (4/3) * ice_cream_cost
    total_money = remaining_money + lunch_cost
    result = total_money
    return result

print(solution())