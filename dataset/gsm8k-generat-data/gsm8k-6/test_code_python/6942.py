def solution():
    # Find the total number of legs of all Mark's animals
    kangaroo_legs = 2 * 23  # each kangaroo has 2 legs
    goat_legs = 4 * (3 * 23)  # there are 3 times as many goats as kangaroos, each goat has 4 legs
    total_legs = kangaroo_legs + goat_legs
    result = total_legs
    return result

print(solution())