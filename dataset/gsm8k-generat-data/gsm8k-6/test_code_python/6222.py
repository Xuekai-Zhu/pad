def solution():
    num_bunnies = 5 * 3  # Jina has 3 times more bunnies than teddies
    num_teddies_with_gift = 5 + 2*num_bunnies  # Jina gets 2 additional teddies for every bunny she has
    total_mascots = num_teddies_with_gift + 1  # add the one koala bear
    result = total_mascots
    return result

print(solution())