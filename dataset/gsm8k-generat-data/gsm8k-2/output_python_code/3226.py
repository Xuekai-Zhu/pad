def solution():
    """Raj's house has an area equal to 1,110 square feet. It has 4 bedrooms that each measure 11 x 11 feet. There are 2 bathrooms that are 6 x 8 feet each. The kitchen and living area complete the home and they have the same sized area. How many square feet is the area of the kitchen?"""
    total_area = 1110
    bedroom_area = 4 * (11 * 11)
    bathroom_area = 2 * (6 * 8)
    living_area = total_area - bedroom_area - bathroom_area
    kitchen_area = living_area / 2
    result = kitchen_area
    return result

print(solution())