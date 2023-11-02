def solution():
    """Frank wants to buy a new lamp for his bedroom. The cost of the cheapest lamp is $20, and the most expensive in the store is 3 times more expensive. How much money would Frank have remaining, if he currently has $90, and he buys the most expensive lamp available?"""
    # Define the cost of the cheapest lamp and the multiplier for the most expensive lamp
    CHEAPEST_LAMP = 20
    MOST_EXPENSIVE_MULTIPLIER = 3

    # Define Frank's available money and calculate the cost of the most expensive lamp
    available_money = 90
    most_expensive_cost = CHEAPEST_LAMP * MOST_EXPENSIVE_MULTIPLIER

    # Calculate Frank's remaining money after buying the most expensive lamp
    remaining_money = available_money - most_expensive_cost

    # Display Frank's remaining money
    result = remaining_money
    return result

print(solution())