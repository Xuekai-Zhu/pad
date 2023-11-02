def solution():
    """Josh has 85 marbles. There are three times as many blue marbles as red while the rest are yellow. If there are 14 red marbles, how many yellow marbles are there?"""
    total_marbles = 85
    red_marbles = 14
    blue_marbles = 3 * red_marbles
    yellow_marbles = total_marbles - red_marbles - blue_marbles
    result = yellow_marbles
    return result

print(solution())