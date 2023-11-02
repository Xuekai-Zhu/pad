def solution():
    """Raj's house has an area equal to 1,110 square feet. It has 4 bedrooms that each measure 11 x 11 feet. There are 2 bathrooms that are 6 x 8 feet each. The kitchen and living area complete the home and they have the same sized area. How many square feet is the area of the kitchen?"""
    # Calculate the area of each bedroom
    bedroom_area = 11 * 11

    # Calculate the total area of all the bedrooms
    total_bedroom_area = bedroom_area * 4

    # Calculate the area of each bathroom
    bathroom_area = 6 * 8

    # Calculate the total area of all the bathrooms
    total_bathroom_area = bathroom_area * 2

    # Calculate the area of the living room
    living_area = (1110 - total_bedroom_area - total_bathroom_area) / 2

    # Calculate the area of the kitchen
    kitchen_area = living_area

    # Display the area of the kitchen
    result = kitchen_area
    return result

print(solution())