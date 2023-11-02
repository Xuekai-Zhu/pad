def solution():
    """A row of houses all share a community space where they put up their clotheslines. There are 2 clotheslines for every house on the street. On the street, there are a total of 11 children and 20 adults. Each child currently has 4 items of clothing on the clotheslines and each adult currently has 3 items of clothing on the clotheslines. If each clothesline can hold 2 items of clothing and all of the clotheslines are full, how many houses are on the street?"""
    # Define the number of clotheslines on the street
    total_clotheslines = (11 * 4) + (20 * 3)

    # Calculate the number of houses on the street based on the number of clotheslines
    num_houses = total_clotheslines // (2 * 2)

    # return the result
    result = num_houses
    return result

print(solution())