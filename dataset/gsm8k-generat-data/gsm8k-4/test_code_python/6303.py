def solution():
    """At least a third of Fred's marbles are dark blue. All of the rest are red, except for 4 that are green. If he has 63 marbles, how many of them are red?"""
    # Define the total number of marbles
    total_marbles = 63

    # Calculate the minimum number of marbles that are dark blue
    dark_blue_min = total_marbles / 3

    # Calculate the maximum number of marbles that are dark blue
    dark_blue_max = total_marbles - 4

    # Calculate the number of marbles that are red
    red_marbles = max(0, total_marbles - dark_blue_max - 4)

    # return the result
    result = red_marbles
    return result

print(solution())