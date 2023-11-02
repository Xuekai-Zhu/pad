def solution():
    """In the jar, there are 7 blue marbles, 11 red marbles, and some yellow marbles. If the chance of randomly picking a yellow marble is 1/4, how many yellow marbles are there?"""
    # Define the number of blue and red marbles
    blue_marbles = 7
    red_marbles = 11

    # Calculate the total number of marbles
    total_marbles = blue_marbles + red_marbles + y_marbles

    # Calculate the probability of picking a yellow marble
    probability_yellow = 1/4

    # Calculate the number of yellow marbles
    y_marbles = round((probability_yellow * total_marbles) - blue_marbles - red_marbles)

    # Display the number of yellow marbles
    result = y_marbles
    return result

print(solution())