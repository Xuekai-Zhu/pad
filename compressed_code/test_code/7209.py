def solution():
    
    roses_per_arrangement = 8
    daisies_per_arrangement = 12
    snapdragons_per_arrangement = 3
    lilies_per_arrangement = 2 * snapdragons_per_arrangement
    flowers_per_arrangement = roses_per_arrangement + daisies_per_arrangement + snapdragons_per_arrangement + lilies_per_arrangement
    arrangements_per_table = 1
    total_tables = 10
    total_flowers = flowers_per_arrangement * arrangements_per_table * total_tables
    result = total_flowers
    return result

print(solution())