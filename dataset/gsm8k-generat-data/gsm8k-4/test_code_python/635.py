def solution():
    """A baker has 10 cheesecakes on the display while 15 more are still in the fridge. If the baker has sold 7 cheesecakes from the display, how many more cheesecakes are left to be sold?"""
    # Define the initial number of cheesecakes
    initial_cheesecakes = 10 + 15

    # Define the number of cheesecakes sold
    sold_cheesecakes = 7

    # Calculate the number of cheesecakes left
    remaining_cheesecakes = initial_cheesecakes - sold_cheesecakes

    result = remaining_cheesecakes
    return result

print(solution())