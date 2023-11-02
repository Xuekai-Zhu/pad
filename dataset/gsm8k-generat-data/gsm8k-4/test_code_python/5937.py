def solution():
    """Beth has 72 marbles of three colors. Each color has the same amount of marbles. If Beth loses 5 red, twice as many blue, and three times as many yellow ones than red ones, how many marbles does she have left?"""
    # Define the total number of marbles and the number of marbles per color
    total_marbles = 72
    marbles_per_color = total_marbles // 3

    # Define the number of marbles lost per color
    red_lost = 5
    blue_lost = 2 * red_lost
    yellow_lost = 3 * red_lost

    # Calculate the number of marbles remaining per color
    red_remaining = marbles_per_color - red_lost
    blue_remaining = marbles_per_color - blue_lost
    yellow_remaining = marbles_per_color - yellow_lost

    # Calculate the total number of marbles remaining
    total_remaining = red_remaining + blue_remaining + yellow_remaining

    # return the result
    result = total_remaining
    return result

print(solution())