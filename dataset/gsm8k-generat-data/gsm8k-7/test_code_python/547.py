def solution():
    bedroom_time = 4
    kitchen_time = bedroom_time * 1.5    # 50% longer than each bedroom
    living_room_time = (bedroom_time + kitchen_time) * 2    # twice as much time as everything else combined

    total_bedroom_time = bedroom_time * 3   # 3 bedrooms
    total_kitchen_time = kitchen_time
    total_living_room_time = living_room_time

    total_time = total_bedroom_time + total_kitchen_time + total_living_room_time
    result = total_time
    return result

print(solution())