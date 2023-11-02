def solution():
    """Jina likes to collect mascots. She has 5 teddies, 3 times more bunnies, and a koala bear. Her mom decided to give her two additional teddies for every bunny she has. How many mascots Jina has in total?"""
    teddies = 5
    bunnies = 3 * teddies
    koalas = 1
    additional_teddies = 2 * bunnies
    total_mascots = teddies + bunnies + koalas + additional_teddies
    result = total_mascots
    return result

print(solution())