def solution():
    """In the jar, there are 7 blue marbles, 11 red marbles, and some yellow marbles. If the chance of randomly picking a yellow marble is 1/4, how many yellow marbles are there?"""
    total_marbles = 7 + 11 + y
    yellow_chance = 1 / 4
    yellow_marbles = (total_marbles * yellow_chance) - (7 + 11)
    result = yellow_marbles
    return result

print(solution())