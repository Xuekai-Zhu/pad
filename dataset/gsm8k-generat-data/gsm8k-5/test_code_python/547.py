def solution():
    bedroom_time = 4  # Each bedroom takes 4 hours
    kitchen_time = bedroom_time * 1.5  # The kitchen takes 50% longer than each bedroom
    living_room_time = (bedroom_time + kitchen_time) * 2  # The living room took twice as much time as everything else combined

    # Calculate the total time taken for renovating the house
    total_time = (bedroom_time * 3) + kitchen_time + living_room_time
    result = total_time
    return result

print(solution())