def solution():
    """Beth has 72 marbles of three colors. Each color has the same amount of marbles. If Beth loses 5 red, twice as many blue, and three times as many yellow ones than red ones, how many marbles does she have left?"""
    # Calculate the initial number of marbles per color
    num_per_color = 72 / 3

    # Calculate the number of marbles Beth loses
    lost_red = 5
    lost_blue = 2 * lost_red
    lost_yellow = 3 * lost_red

    # Calculate the new number of marbles per color
    red_marbles = num_per_color - lost_red
    blue_marbles = num_per_color - lost_blue
    yellow_marbles = num_per_color - lost_yellow

    # Calculate the total number of marbles Beth has left
    total_marbles = red_marbles + blue_marbles + yellow_marbles

    # Display the total number of marbles Beth has left
    result = total_marbles
    return result

print(solution())