def solution():
    """Leticia, Scarlett, and Percy decide to eat at a Greek restaurant for lunch. The prices for their dishes cost $10, $13, and $17, respectively. If the trio gives the waiter a 10% tip, how much gratuity should the waiter receive in dollars?"""
    # Define the prices of the dishes
    dish1_price = 10
    dish2_price = 13
    dish3_price = 17

    # Calculate the total cost of the meal
    total_cost = dish1_price + dish2_price + dish3_price

    # Calculate the 10% tip
    tip = total_cost * 0.1

    # return the result
    result = tip
    return result

print(solution())