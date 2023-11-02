def solution():
    """There are 50 marbles in a box which has a mixture of white, red and blue marbles. There were originally 20 white marbles and an equal number of red and blue marbles. Jack removes a number of marbles equal to double the difference between the number of white marbles and the number of blue marbles. How many marbles are left in the box?"""
    # Define the initial number of white marbles
    white_marbles = 20

    # Calculate the initial number of red and blue marbles
    red_blue_marbles = (50 - white_marbles) / 2

    # Calculate the number of marbles Jack removes
    removed_marbles = 2 * (white_marbles - red_blue_marbles)

    # Calculate the number of marbles left in the box
    remaining_marbles = 50 - removed_marbles

    result = remaining_marbles
    return result

print(solution())