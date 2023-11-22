def solution():
    
    # Define the number of rooms and the time it takes to clean each room
    num_rooms = 90
    time_per_room = 20 / num_rooms

    # Calculate the total time it would take to clean one-half of the rooms
    total_time = time_per_room * num_rooms / 2

    # Convert the total time to hours
    total_time_hours = total_time / 60

    # Display the total time in hours
    result = total_time_hours
    return result

print(solution())