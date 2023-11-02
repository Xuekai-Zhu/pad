def solution():
    """Frank wants to buy a new lamp for his bedroom. The cost of the cheapest lamp is $20, and the most expensive in the store is 3 times more expensive. How much money would Frank have remaining, if he currently has $90, and he buys the most expensive lamp available?"""
    # Define the cost of the cheapest lamp and the maximum cost
    cheapest_lamp = 20
    max_cost = cheapest_lamp * 3

    # Define Frank's current balance and calculate how much he would have left after buying the most expensive lamp
    current_balance = 90
    remaining_balance = current_balance - max_cost

    # Return the remaining balance
    result = remaining_balance
    return result

print(solution())