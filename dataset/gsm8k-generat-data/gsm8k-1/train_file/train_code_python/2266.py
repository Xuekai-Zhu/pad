def solution():
    """A row of houses all share a community space where they put up their clotheslines. There are 2 clotheslines for every house on the street. On the street, there are a total of 11 children and 20 adults. Each child currently has 4 items of clothing on the clotheslines and each adult currently has 3 items of clothing on the clotheslines. If each clothesline can hold 2 items of clothing and all of the clotheslines are full, how many houses are on the street?"""
    total_clotheslines = (11 * 4) + (20 * 3)
    clotheslines_per_house = 2
    total_houses = total_clotheslines // (clotheslines_per_house * 2)
    result = total_houses
    return result

print(solution())