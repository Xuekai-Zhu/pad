def solution():
    """There are 19 marbles in a bowl, 5 of which are yellow. The remainder are split into blue marbles and red marbles in the ratio 3:4 respectively. How many more red marbles than yellow marbles are there?"""
    total_marbles = 19
    yellow_marbles = 5
    remaining_marbles = total_marbles - yellow_marbles
    blue_marbles = remaining_marbles * 3 / 7
    red_marbles = remaining_marbles * 4 / 7
    difference = red_marbles - yellow_marbles
    result = difference
    return result

print(solution())