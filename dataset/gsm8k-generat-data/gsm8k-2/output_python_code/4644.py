def solution():
    """There are 50 marbles in a box which has a mixture of white, red and blue marbles. There were originally 20 white marbles and an equal number of red and blue marbles. Jack removes a number of marbles equal to double the difference between the number of white marbles and the number of blue marbles. How many marbles are left in the box?"""
    total_marbles = 50
    white_marbles = 20
    red_marbles = blue_marbles = (total_marbles - white_marbles) / 2
    removed_marbles = 2 * (white_marbles - blue_marbles)
    marbles_left = total_marbles - removed_marbles
    result = marbles_left
    return result

print(solution())