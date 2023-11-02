def solution():
    """Abigail thinks she has some lost some money out of her purse. She had $11 in her purse at the start of the day, and she spent $2 in a store. If she now has $3 left, how much money has she lost?"""
    # Define the initial amount in Abigail's purse
    initial_amount = 11

    # Define the amount Abigail spent in the store
    spent_amount = 2

    # Define the current amount in Abigail's purse
    current_amount = 3

    # Calculate the amount of money Abigail lost
    lost_amount = initial_amount - spent_amount - current_amount

    result = lost_amount
    return result

print(solution())