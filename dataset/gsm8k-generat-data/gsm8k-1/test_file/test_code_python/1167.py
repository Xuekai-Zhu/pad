def solution():
    """Tom has 4 bedrooms in his house. They measure 20 by 12 feet each. The living room is 5 times bigger than one bedroom. The rest of the house is 1000 square feet. What is the total area, in square feet, of the house?"""
    bedroom_length = 20
    bedroom_width = 12
    num_bedrooms = 4
    living_room_multiple = 5
    living_room_length = bedroom_length * living_room_multiple
    living_room_width = bedroom_width * living_room_multiple
    living_room_area = living_room_length * living_room_width
    bedroom_area = bedroom_length * bedroom_width
    total_bedroom_area = num_bedrooms * bedroom_area
    rest_of_house_area = 1000
    total_area = living_room_area + total_bedroom_area + rest_of_house_area
    result = total_area
    
    return result

print(solution())