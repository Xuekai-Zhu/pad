def solution():
    """Jar A has 28 marbles. Jar B has 12 more marbles than jar A. Jar C has twice as many marbles as jar B.
    How many marbles are there altogether?"""
    jar_a = 28
    jar_b = jar_a + 12
    jar_c = 2 * jar_b
    total_marbles = jar_a + jar_b + jar_c
    result = total_marbles
    return result

print(solution())