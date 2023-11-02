def solution():
    """Nancy replaced all of the old vinyl tiles in her bathroom with new hardwood flooring. She replaced flooring in two areas of the bathroom: a 10 foot by 10 foot central area, and a 6 foot by 4 foot hallway. How many square feet of hardwood flooring did Nancy install in her bathroom?"""
    # Define the dimensions of the central area and the hallway
    central_area_length = 10
    central_area_width = 10
    hallway_length = 6
    hallway_width = 4

    # Calculate the area of the central area and the hallway
    central_area = central_area_length * central_area_width
    hallway = hallway_length * hallway_width

    # Calculate the total area of hardwood flooring installed
    total_area = central_area + hallway

    # Return the result
    result = total_area
    return result

print(solution())