def solution():
    """Ice cream costs $2.00 and toppings cost $0.50 per topping. How much does a sundae with 10 toppings cost?"""
    # Define the cost of ice cream and toppings
    ice_cream_cost = 2.00
    topping_cost = 0.50

    # Calculate the total cost of a sundae with 10 toppings
    total_cost = ice_cream_cost + (topping_cost * 10)

    # return the result
    result = total_cost
    return result

print(solution())