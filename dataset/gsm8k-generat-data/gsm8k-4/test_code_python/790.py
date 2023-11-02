def solution():
    """Zion made a triangular-shaped house of cards with the base having a measurement of 40 centimeters and a height of 20 centimeters. If two of his friends also built similar shaped houses, what's the total area of the triangular houses that Zion and his friends made (the area of a triangle is 1/2 * width * height)?"""
    # Define the dimensions of the house of cards
    base = 40
    height = 20

    # Calculate the area of Zion's triangular house of cards
    zion_area = 0.5 * base * height

    # Calculate the area of one friend's triangular house of cards
    friend_area = zion_area

    # Calculate the total area of the three triangular houses of cards
    total_area = zion_area + (2 * friend_area)

    result = total_area
    return result

print(solution())