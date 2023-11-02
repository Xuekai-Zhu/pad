def solution():
    # Calculate the total number of clotheslines on the street
    total_clotheslines = (11 * 4 + 20 * 3) / 2  # each clothesline can hold 2 items of clothing

    # Calculate the total number of houses on the street
    total_houses = total_clotheslines / 2  # there are 2 clotheslines for every house

    result = total_houses
    return result

print(solution())