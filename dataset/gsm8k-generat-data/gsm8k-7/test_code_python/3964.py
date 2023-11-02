def solution():
    num_rooms = 6
    room_capacity = 80
    occupancy_percent = 2/3
    total_capacity = num_rooms * room_capacity

    # Calculate the number of people in the conference center
    num_people = total_capacity * occupancy_percent
    result = num_people
    return result

print(solution())