def solution():
    central_area_length = 10
    central_area_width = 10
    hallway_length = 6
    hallway_width = 4
    
    # Calculate the area of the central area
    central_area = central_area_length * central_area_width
    
    # Calculate the area of the hallway
    hallway_area = hallway_length * hallway_width
    
    # Calculate the total area of hardwood flooring installed
    total_area = central_area + hallway_area
    result = total_area
    return result

print(solution())