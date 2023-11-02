def solution():
    # Calculate the total number of clotheslines
    total_clotheslines = (11*4 + 20*3) / 2  # 11 children, each with 4 items and 20 adults, each with 3 items

    # Calculate the total number of houses
    total_houses = total_clotheslines / 2  # 2 clotheslines per house

    result = total_houses
    return result

print(solution())