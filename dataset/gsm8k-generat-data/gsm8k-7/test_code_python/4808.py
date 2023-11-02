def solution():
    bottle_size = 1.5  # quarts
    can_size = 12  # ounces

    # Convert bottle size to ounces
    bottle_size_oz = bottle_size * 32

    total_water = bottle_size_oz + can_size
    result = total_water
    return result

print(solution())