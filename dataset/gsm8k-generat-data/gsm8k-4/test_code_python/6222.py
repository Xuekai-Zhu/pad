def solution():
    """Jina likes to collect mascots. She has 5 teddies, 3 times more bunnies, and a koala bear. Her mom decided to give her two additional teddies for every bunny she has. How many mascots Jina has in total?"""
    # Define the number of teddies Jina has
    teddies = 5

    # Define the number of bunnies Jina has
    bunnies = 3 * teddies

    # Define the number of koalas Jina has
    koalas = 1

    # Calculate the number of additional teddies Jina will receive for her bunnies
    additional_teddies = 2 * bunnies

    # Calculate the total number of mascots Jina has
    total_mascots = teddies + bunnies + koalas + additional_teddies

    # return the result
    result = total_mascots
    return result

print(solution())