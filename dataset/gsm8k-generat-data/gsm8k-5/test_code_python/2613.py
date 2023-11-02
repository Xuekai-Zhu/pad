def solution():
    starting_amount = 87  # Tony starts with $87
    cheese_price = 7  # Cheese costs $7 a pound
    beef_price = 5  # Beef costs $5 a pound
    remaining_amount = 61  # After buying both items, Tony has $61 left

    # Calculate the number of pounds of beef Tony buys
    beef_cost = starting_amount - remaining_amount
    beef_pounds = beef_cost / beef_price

    # Calculate the cost of cheese Tony buys
    cheese_cost = starting_amount - beef_cost - remaining_amount

    # Calculate the number of pounds of cheese Tony buys
    cheese_pounds = cheese_cost / cheese_price
    result = cheese_pounds
    return result

print(solution())