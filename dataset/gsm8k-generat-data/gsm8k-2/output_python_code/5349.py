def solution():
    """Katie has 13 pink marbles. She has 9 fewer orange marbles than pink marbles. She has 4 times as many purple marbles as orange marbles. How many marbles does Katie have in all?"""
    pink_marbles = 13
    orange_marbles = pink_marbles - 9
    purple_marbles = 4 * orange_marbles
    total_marbles = pink_marbles + orange_marbles + purple_marbles
    result = total_marbles
    return result

print(solution())