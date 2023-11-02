def solution():
    """Zion made a triangular-shaped house of cards with the base having a measurement of 40 centimeters and a height of 20 centimeters. If two of his friends also built similar shaped houses, what's the total area of the triangular houses that Zion and his friends made (the area of a triangle is 1/2 * width * height)?"""
    base = 40
    height = 20
    area_zion = base * height / 2
    area_friends = area_zion * 2
    total_area = area_zion + area_friends
    result = total_area
    return result

print(solution())