def solution():
    """There are 12 carpets in house 1, 20 carpets in house 2, and 10 carpets in house 3. If house 4 has twice as many carpets as house 3, how many carpets do all 4 houses have in total?"""
    carpets_house1 = 12
    carpets_house2 = 20
    carpets_house3 = 10
    carpets_house4 = 2 * carpets_house3
    total_carpets = carpets_house1 + carpets_house2 + carpets_house3 + carpets_house4
    result = total_carpets
    return result

print(solution())