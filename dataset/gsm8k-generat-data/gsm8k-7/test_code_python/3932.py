def solution():
    total_time_vacuuming = 2 * 60  # convert hours to minutes
    time_per_room = 20
    num_rooms = total_time_vacuuming // time_per_room
    result = num_rooms
    return result

print(solution())