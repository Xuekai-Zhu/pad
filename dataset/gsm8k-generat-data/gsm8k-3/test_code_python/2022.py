def solution():
    """Dana normally drinks a 500 ml bottle of soda each day. Since the 500 ml bottles are currently out of stock at the store, she buys a 2-liter bottle of soda instead. If Dana continues to drink 500 ml of soda each day, how long will the 2-liter bottle of soda last? There are 1,000 ml in 1 liter."""
    # Define the size of the 2-liter bottle in ml
    BOTTLE_SIZE = 2000

    # Define the amount of soda Dana drinks per day
    DAILY_AMOUNT = 500

    # Calculate the number of days the 2-liter bottle will last
    days_lasts = BOTTLE_SIZE / DAILY_AMOUNT

    # Display the number of days
    result = days_lasts
    return result

print(solution())