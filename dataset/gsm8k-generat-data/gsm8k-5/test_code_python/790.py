def solution():
    # Calculate the area of Zion's house of cards
    area_zion = 0.5 * 40 * 20

    # Calculate the area of each of his friends' house of cards, assuming they have the same measurements
    area_friends = 0.5 * 40 * 20

    # Calculate the total area of the triangular houses
    total_area = area_zion + (2 * area_friends)
    result = total_area
    return result

print(solution())