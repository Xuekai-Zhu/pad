def solution():
    
    # Define the dimensions of each bedroom and living room
    bedroom_width = 20
    bedroom_length = 12
    living_room_width = bedroom_width * 5

    # Calculate the total area of the house
    total_area = bedroom_width * bedroom_length * 4 + living_room_width * 1000

    # return the result
    result = total_area
    return result

print(solution())