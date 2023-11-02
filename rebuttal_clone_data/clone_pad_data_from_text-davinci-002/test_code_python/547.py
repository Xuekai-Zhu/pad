def solution():
    time_per_bedroom = 4
    time_per_kitchen = time_per_bedroom * 1.5
    time_per_living_room = (time_per_bedroom * 3) + time_per_kitchen
    total_time = (time_per_bedroom * 3) + time_per_kitchen + time_per_living_room
    result = total_time
    return result

print(solution())