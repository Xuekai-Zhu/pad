def solution():
    # Calculate the area of Zion's triangular house of cards
    zion_area = (1/2) * 40 * 20

    # Calculate the area of each of his friend's triangular houses of cards
    friend_area = (1/2) * 40 * 20

    # Calculate the total area of the three houses of cards
    total_area = zion_area + (2 * friend_area)
    result = total_area
    return result

print(solution())