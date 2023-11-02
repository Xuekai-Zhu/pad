def solution():
    """At least a third of Fred's marbles are dark blue. All of the rest are red, except for 4 that are green. If he has 63 marbles, how many of them are red?"""
    # Define the minimum percentage of marbles that are dark blue and the number of green marbles
    MIN_BLUE_PERCENTAGE = 1/3
    GREEN_MARBLES = 4

    # Calculate the minimum number of blue marbles
    min_blue_marbles = round(MIN_BLUE_PERCENTAGE * 63)

    # Calculate the total number of non-blue marbles
    non_blue_marbles = 63 - min_blue_marbles

    # Calculate the total number of red marbles
    red_marbles = non_blue_marbles - GREEN_MARBLES

    # Display the total number of red marbles
    result = red_marbles
    return result

print(solution())