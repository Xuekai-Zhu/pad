def solution():
    """George collected 50 marbles in white, yellow, green, and red. Half of them are white, and 12 are yellow. There are 50% fewer green balls than yellow balls. How many marbles are red?"""
    total_marbles = 50
    white_marbles = total_marbles / 2
    yellow_marbles = 12
    green_marbles = yellow_marbles * 0.5
    red_marbles = total_marbles - white_marbles - yellow_marbles - green_marbles
    result = red_marbles
    return result

print(solution())