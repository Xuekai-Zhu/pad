def solution():
    base = 40
    height = 20

    # Calculate the area of Zion's triangular-shaped house of cards
    zion_area = 0.5 * base * height

    # Calculate the area of one of his friend's triangular-shaped house of cards
    friend_area = zion_area

    # Calculate the total area of the triangular houses that Zion and his friends made
    total_area = (zion_area + friend_area) * 2  # multiplied by 2 since there are 3 houses in total
    result = total_area
    return result

print(solution())