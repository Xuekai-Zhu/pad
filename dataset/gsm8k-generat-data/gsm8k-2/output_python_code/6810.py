def solution():
    """There are 24 marbles in a jar. Half are blue. There are 6 red marbles. The rest of the marbles are orange. How many orange marbles are there?"""
    total_marbles = 24
    blue_marbles = total_marbles / 2
    red_marbles = 6
    orange_marbles = total_marbles - blue_marbles - red_marbles
    result = orange_marbles
    return result

print(solution())