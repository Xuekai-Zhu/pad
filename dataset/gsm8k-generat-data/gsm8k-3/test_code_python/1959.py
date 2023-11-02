def solution():
    """Abigail thinks she has some lost some money out of her purse. She had $11 in her purse at the start of the day, and she spent $2 in a store. If she now has $3 left, how much money has she lost?"""
    # Define the amount of money Abigail had at the start of the day
    starting_amount = 11

    # Define the amount of money Abigail spent at the store
    spending = 2

    # Define the amount of money Abigail has left
    remaining_amount = 3

    # Calculate the amount of money Abigail lost
    lost_amount = starting_amount - spending - remaining_amount

    # Display the amount of money Abigail lost
    result = lost_amount
    return result

print(solution())