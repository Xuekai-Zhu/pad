def solution():
    """Laura bought 2 pairs of pants for $54 each and 4 shirts for $33 each. She gave $250 to the cashier. So how much change did she take?"""
    # Define the prices of pants and shirts
    pants_price = 54
    shirts_price = 33

    # Calculate the total amount spent
    total_spent = (2 * pants_price) + (4 * shirts_price)

    # Calculate the change received
    change = 250 - total_spent

    result = change
    return result

print(solution())