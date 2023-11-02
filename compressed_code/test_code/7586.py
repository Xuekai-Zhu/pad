def solution():
    
    total_clotheslines = (11 * 4) + (20 * 3)
    clotheslines_per_house = 2
    total_houses = total_clotheslines // (clotheslines_per_house * 2)
    result = total_houses
    return result

print(solution())