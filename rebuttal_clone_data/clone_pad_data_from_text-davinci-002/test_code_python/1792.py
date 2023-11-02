def solution():
    roses_needed = 8
    daisies_needed = 12
    snapdragons_needed = 3
    lilies_needed = (roses_needed * 2)
    total_flowers_needed = (roses_needed + daisies_needed + snapdragons_needed + lilies_needed) * 10
    result = total_flowers_needed
    return result

print(solution())