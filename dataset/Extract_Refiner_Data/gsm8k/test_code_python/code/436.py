def solution():
    
    # Define the area of the bedroom in square feet
    bedroom_area = 360

    # Convert the length of the room from yards to feet
    room_length = 3 * 3

    # Calculate the perimeter of the room in square feet
    room_perimeter = bedroom_area / room_length

    # Display the perimeter of the room
    result = room_perimeter
    return result

print(solution())