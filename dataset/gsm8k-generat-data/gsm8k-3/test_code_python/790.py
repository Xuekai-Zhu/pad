def solution():
    """Zion made a triangular-shaped house of cards with the base having a measurement of 40 centimeters and a height of 20 centimeters. If two of his friends also built similar shaped houses, what's the total area of the triangular houses that Zion and his friends made (the area of a triangle is 1/2 * width * height)?"""
    # Define the base and height of Zion's triangular house of cards
    base_zion = 40
    height_zion = 20

    # Calculate the area of Zion's triangular house of cards
    area_zion = 0.5 * base_zion * height_zion

    # Calculate the area of the triangular houses of Zion's friends
    base_friend = base_zion  # assume all houses have the same base measurement
    height_friend = height_zion  # assume all houses have the same height measurement
    area_friend = 0.5 * base_friend * height_friend

    # Calculate the total area of all triangular houses
    total_area = 3 * area_friend  # there are three triangular houses in total

    # Display the total area
    result = total_area
    return result

print(solution())