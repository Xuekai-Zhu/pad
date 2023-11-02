def solution():
    """Mary is making ice cubes with fruit frozen in them for a cocktail party. She makes some strawberry cubes, and a number of blueberry cubes equal to 5 times the number of strawberry cubes minus 4. If she makes 116 ice cubes total, how many blueberry cubes does she make?"""
    total_cubes = 116
    blueberry_multiplier = 5
    blueberry_offset = 4
    strawberry_cubes = total_cubes / (blueberry_multiplier + 1)
    blueberry_cubes = (blueberry_multiplier * strawberry_cubes) - blueberry_offset
    result = blueberry_cubes
    return result

print(solution())