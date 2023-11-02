def solution():
    """Jina likes to collect mascots. She has 5 teddies, 3 times more bunnies, and a koala bear. Her mom decided to give her two additional teddies for every bunny she has. How many mascots Jina has in total?"""
    teddies = 5
    bunnies = 3 * teddies
    koala_bear = 1
    teddies_per_bunny = 2
    total_teddies = teddies + (bunnies * teddies_per_bunny) + koala_bear
    result = total_teddies
    return result

print(solution())