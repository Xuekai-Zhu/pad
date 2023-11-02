def solution():
    
    # Define the length of the room in yards
    room_length_yards = 3

    # Convert the length of the room to feet
    room_length_feet = room_length_yards * 3

    # Calculate the perimeter of the room
    room_perimeter = room_length_feet / 360

    # Display the perimeter of the room
    result = room_perimeter
    return result

print(solution())