def solution():
    # Calculate the number of rooms in Susie's house
    total_vacuuming_time = 2*60  # time taken to vacuum the whole house in minutes
    time_per_room = 20  # time taken to vacuum each room in minutes
    num_rooms = total_vacuuming_time // time_per_room
    result = num_rooms
    return result

print(solution())