def solution():
    """Raj's house has an area equal to 1,110 square feet. It has 4 bedrooms that each measure 11 x 11 feet. There are 2 bathrooms that are 6 x 8 feet each. The kitchen and living area complete the home and they have the same sized area. How many square feet is the area of the kitchen?"""
    total_area = 1110
    bedrooms_area = 4 * (11 * 11)
    bathrooms_area = 2 * (6 * 8)
    kitchen_living_area = total_area - bedrooms_area - bathrooms_area
    kitchen_area = kitchen_living_area / 2 
    result = kitchen_area
    return result

print(solution())