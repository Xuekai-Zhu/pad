def solution():
    collin_flowers = 25
    ingrid_flowers = 33
    flowers_given = ingrid_flowers / 3
    total_flowers = collin_flowers + flowers_given
    petals_per_flower = 4
    total_petals = total_flowers * petals_per_flower
    result = total_petals
    return result

print(solution())