def solution():
    """Fred has 38 red marbles, half as many green ones, and the rest are dark blue. If he has 63 marbles, how many of them are dark blue?"""
    red_marbles = 38
    green_marbles = red_marbles / 2
    total_marbles = 63
    dark_blue_marbles = total_marbles - red_marbles - green_marbles
    result = dark_blue_marbles
    return result

print(solution())