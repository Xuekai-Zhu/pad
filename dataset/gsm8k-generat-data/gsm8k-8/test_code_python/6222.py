def solution():
    teddy_count = 5
    bunny_count = 3 * teddy_count
    koala_count = 1
    extra_teddies_per_bunny = 2

    # Calculate the total number of teddies Jina has after getting the additional ones from her mom
    total_teddies = teddy_count + extra_teddies_per_bunny * bunny_count

    # Calculate the total number of mascots Jina has
    total_mascots = total_teddies + bunny_count + koala_count
    result = total_mascots
    return result

print(solution())