def solution():
    """Courtney liked to collect marbles. She kept them in mason jars. One jar had 80 marbles. Her second jar had twice that amount. She just started her third jar which currently has 1/4 the amount of her first jar. How many marbles does she have in total?"""
    jar1 = 80
    jar2 = jar1 * 2
    jar3 = jar1 / 4
    total_marbles = jar1 + jar2 + jar3
    result = total_marbles
    return result

print(solution())