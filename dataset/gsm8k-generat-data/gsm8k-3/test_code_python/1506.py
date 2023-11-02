def solution():
    """Tina made a large pan of brownies and cut it into 24 pieces.  She had one with lunch and dinner every day for 5 days.  Her husband snagged one per day for 5 days to take to work.  They shared 4 with dinner guests.  How many brownies were left?"""
    # Define the total number of brownies in the pan
    total_brownies = 24

    # Calculate the number of brownies Tina and her husband ate
    tina_brownies = 2 * 5
    husband_brownies = 5
    total_eaten = tina_brownies + husband_brownies

    # Calculate the number of brownies shared with dinner guests
    shared_brownies = 4

    # Calculate the number of brownies left
    left_brownies = total_brownies - total_eaten - shared_brownies

    # Display the number of brownies left
    result = left_brownies
    return result

print(solution())