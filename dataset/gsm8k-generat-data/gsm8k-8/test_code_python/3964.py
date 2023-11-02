def solution():
    # Define the capacity of each room
    room_capacity = 80

    # Calculate the total capacity of the conference center
    total_capacity = room_capacity * 6

    # Calculate the current number of people in the conference center
    current_capacity = total_capacity * (2/3)

    result = current_capacity
    return result

print(solution())