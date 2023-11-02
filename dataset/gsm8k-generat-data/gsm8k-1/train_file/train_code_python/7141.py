def solution():
    """Frank wants to buy a new lamp for his bedroom. The cost of the cheapest lamp is $20, and the most expensive in the store is 3 times more expensive. How much money would Frank have remaining, if he currently has $90, and he buys the most expensive lamp available?"""
    cheapest_lamp = 20
    most_expensive_lamp = cheapest_lamp * 3
    current_money = 90
    remaining_money = current_money - most_expensive_lamp
    result = remaining_money
    return result

print(solution())