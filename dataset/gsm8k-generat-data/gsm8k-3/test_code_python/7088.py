def solution():
    """Ice cream costs $2.00 and toppings cost $0.50 per topping. How much does a sundae with 10 toppings cost?"""
    # Define the cost of ice cream and toppings
    ICE_CREAM_COST = 2.00
    TOPPING_COST = 0.50

    # Define the number of toppings
    NUM_TOPPINGS = 10

    # Calculate the total cost of the sundae
    total_cost = ICE_CREAM_COST + (NUM_TOPPINGS * TOPPING_COST)

    # Display the total cost of the sundae
    result = total_cost
    return result

print(solution())