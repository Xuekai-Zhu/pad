def solution():
    total_time = 2 * 60  # Susie takes 2 hours to vacuum the whole house
    time_per_room = 20  # Susie can vacuum each room in 20 minutes

    # Calculate the total number of rooms in Susie's house
    total_rooms = int(total_time / time_per_room)

    result = total_rooms
    return result

print(solution())