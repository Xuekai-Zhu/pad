def solution():
    """Dana normally drinks a 500 ml bottle of soda each day. Since the 500 ml bottles are currently out of stock at the store, she buys a 2-liter bottle of soda instead. If Dana continues to drink 500 ml of soda each day, how long will the 2-liter bottle of soda last? There are 1,000 ml in 1 liter."""
    # Define the amount of soda Dana drinks each day
    daily_soda = 500

    # Define the size of the 2-liter bottle of soda
    bottle_size = 2000

    # Calculate how many days the 2-liter bottle will last
    days = bottle_size / daily_soda

    result = days
    return result

print(solution())