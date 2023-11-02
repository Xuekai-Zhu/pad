def solution():
    """Frank went to a shop to buy some food for his breakfast. He bought 10 buns for $0.1 each, two bottles of milk, for $2 each, and a carton of eggs, which was three times more expensive than one bottle of milk. How much did Frank pay for his breakfast shopping?"""
    # Define the price of the buns, milk and eggs
    buns_price = 0.1
    milk_price = 2
    eggs_price = 3 * milk_price

    # Calculate the total cost of the buns
    buns_cost = 10 * buns_price

    # Calculate the total cost of the milk
    milk_cost = 2 * milk_price

    # Calculate the cost of the eggs
    eggs_cost = eggs_price

    # Calculate the total cost
    total_cost = buns_cost + milk_cost + eggs_cost

    # Return the result
    result = total_cost
    return result

print(solution())