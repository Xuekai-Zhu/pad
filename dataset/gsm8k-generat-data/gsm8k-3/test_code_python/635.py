def solution():
    """A baker has 10 cheesecakes on the display while 15 more are still in the fridge. If the baker has sold 7 cheesecakes from the display, how many more cheesecakes are left to be sold?"""
    # Define the initial number of cheesecakes
    initial_cheesecakes = 10 + 15

    # Define the number of cheesecakes sold
    cheesecakes_sold = 7

    # Calculate the number of cheesecakes left
    cheesecakes_left = initial_cheesecakes - cheesecakes_sold

    # Display the number of cheesecakes left
    result = cheesecakes_left
    return result

print(solution())