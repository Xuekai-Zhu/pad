def solution():
    """Jar A has 28 marbles. Jar B has 12 more marbles than jar A. Jar C has twice as many marbles as jar B. How many marbles are there altogether?"""
    marbles_in_A = 28
    marbles_in_B = marbles_in_A + 12
    marbles_in_C = 2 * marbles_in_B
    total_marbles = marbles_in_A + marbles_in_B + marbles_in_C
    result = total_marbles
    return result

print(solution())