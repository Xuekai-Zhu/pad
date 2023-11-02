def solution():
    """A jar full of marbles is sitting on a table. Half of the marbles are blue, a quarter of them are red, 27 of them are green, and 14 of them are yellow. How many marbles are in the jar?"""
    # Calculate the fraction of marbles that are not blue or red
    non_blue_or_red = 1 - 0.5 - 0.25

    # Calculate the total number of marbles
    total_marbles = 27 / non_blue_or_red

    # Calculate the number of blue marbles
    blue_marbles = total_marbles * 0.5

    # Calculate the number of red marbles
    red_marbles = total_marbles * 0.25

    # Calculate the number of green marbles
    green_marbles = 27

    # Calculate the number of yellow marbles
    yellow_marbles = 14

    # Calculate the total number of marbles
    total_marbles = blue_marbles + red_marbles + green_marbles + yellow_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())