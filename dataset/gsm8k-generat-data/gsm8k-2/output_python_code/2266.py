def solution():
    """A row of houses all share a community space where they put up their clotheslines. There are 2 clotheslines for every house on the street. On the street, there are a total of 11 children and 20 adults. Each child currently has 4 items of clothing on the clotheslines and each adult currently has 3 items of clothing on the clotheslines. If each clothesline can hold 2 items of clothing and all of the clotheslines are full, how many houses are on the street?"""
    total_clothes = (11 * 4) + (20 * 3)
    total_clotheslines = total_clothes / 2
    houses = total_clotheslines / 2
    result = houses
    return result

print(solution())