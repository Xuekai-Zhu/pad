def solution():
    """At a softball game, three players are having a sunflower eating contest. The first player eats 78 seeds. The second eats 53 seeds. The third eats 30 more seeds than the second. How many do they eat in total?"""
    player1_seeds = 78
    player2_seeds = 53
    player3_seeds = player2_seeds + 30
    total_seeds = player1_seeds + player2_seeds + player3_seeds
    result = total_seeds
    return result

print(solution())