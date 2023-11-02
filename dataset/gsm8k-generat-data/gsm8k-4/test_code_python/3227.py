def solution():
    """Raj's house has an area equal to 1,110 square feet. It has 4 bedrooms that each measure 11 x 11 feet. There are 2 bathrooms that are 6 x 8 feet each. The kitchen and living area complete the home and they have the same sized area. How many square feet is the area of the kitchen?"""
    
    # Calculate the total area of the 4 bedrooms
    bedroom_area = 4 * (11 * 11)

    # Calculate the total area of the 2 bathrooms
    bathroom_area = 2 * (6 * 8)

    # Calculate the total area of the house
    total_area = 1110

    # Calculate the total area of the kitchen and living area
    kitchen_area = total_area - bedroom_area - bathroom_area

    # Divide the kitchen area by 2 to get the area of the kitchen alone
    kitchen_alone_area = kitchen_area / 2

    result = kitchen_alone_area
    return result

print(solution())