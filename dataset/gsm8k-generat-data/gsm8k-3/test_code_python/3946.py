def solution():
    """Mother made 2 dozen brownies and placed them on the kitchen counter to cool.  Father smelled the brownies, came into the kitchen and ate 8 of them. Then, their daughter, Mooney, wandered into the kitchen and ate 4 of the brownies. The next morning, Mother made another two dozen brownies and added them to those remaining from the day before.  After that, how many brownies were on the counter?"""
    # Define the number of brownies in one dozen
    DOZEN = 12

    # Initial number of brownies
    initial_brownies = 2 * DOZEN

    # Number of brownies left after Father ate 8
    brownies_left = initial_brownies - 8

    # Number of brownies left after Mooney ate 4
    brownies_left -= 4

    # Number of brownies after adding another 2 dozen
    final_brownies = brownies_left + 2 * DOZEN

    # Display the final number of brownies
    result = final_brownies
    return result

print(solution())