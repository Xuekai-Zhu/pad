def solution():
    num_bedrooms = 3
    bedroom_time = 20  # minutes

    living_room_time = num_bedrooms * bedroom_time  # minutes
    bathroom_time = 2 * living_room_time  # minutes
    inside_time = living_room_time + bathroom_time  # minutes
    outside_time = 2 * inside_time  # minutes

    total_time = (num_bedrooms * bedroom_time + living_room_time + bathroom_time + outside_time) / 60  # hours
    time_per_person = total_time / 3

    result = time_per_person
    return result

print(solution())