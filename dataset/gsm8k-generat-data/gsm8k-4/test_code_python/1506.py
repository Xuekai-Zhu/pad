def solution():
    """Tina made a large pan of brownies and cut it into 24 pieces. She had one with lunch and dinner every day for 5 days. Her husband snagged one per day for 5 days to take to work. They shared 4 with dinner guests. How many brownies were left?"""
    # Define the initial number of brownies
    initial_brownies = 24

    # Calculate the number of brownies eaten by Tina
    tina_brownies = 2 * 5

    # Calculate the number of brownies eaten by Tina's husband
    husband_brownies = 5

    # Calculate the number of brownies shared with guests
    guest_brownies = 4

    # Calculate the total number of brownies left
    brownies_left = initial_brownies - tina_brownies - husband_brownies - guest_brownies

    # return the result
    result = brownies_left
    return result

print(solution())