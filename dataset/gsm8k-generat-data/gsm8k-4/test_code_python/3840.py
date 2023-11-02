def solution():
    """Fred has 38 red marbles, half as many green ones, and the rest are dark blue. If he has 63 marbles, how many of them are dark blue?"""
    # Define the number of red marbles
    red_marbles = 38

    # Calculate the number of green marbles
    green_marbles = red_marbles / 2

    # Calculate the total number of red and green marbles
    red_green_marbles = red_marbles + green_marbles

    # Calculate the number of dark blue marbles
    darkblue_marbles = 63 - red_green_marbles

    result = darkblue_marbles
    return result

print(solution())