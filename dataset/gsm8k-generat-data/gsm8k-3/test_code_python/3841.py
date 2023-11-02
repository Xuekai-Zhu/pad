def solution():
    """Laura bought 2 pairs of pants for $54 each and 4 shirts for $33 each. She gave $250 to the cashier. So how much change did she take?"""
    # Define the cost of each pair of pants and shirt
    PANTS_PRICE = 54
    SHIRT_PRICE = 33
    
    # Define the number of pants and shirts bought
    pants_bought = 2
    shirts_bought = 4
    
    # Calculate the total cost of the pants and shirts
    total_cost = (pants_bought * PANTS_PRICE) + (shirts_bought * SHIRT_PRICE)
    
    # Calculate the change Laura should receive
    change = 250 - total_cost
    
    # Display the change
    result = change
    return result

print(solution())