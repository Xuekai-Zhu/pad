def solution():
    """At least a third of Fred's marbles are dark blue. All of the rest are red, except for 4 that are green. If he has 63 marbles, how many of them are red?"""
    total_marbles = 63
    dark_blue_marbles = total_marbles // 3
    green_marbles = 4
    red_marbles = total_marbles - dark_blue_marbles - green_marbles
    result = red_marbles
    return result

print(solution())