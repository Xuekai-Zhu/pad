def solution():
    # Calculate the time to renovate each bedroom
    bedroom_time = 4
    kitchen_time = bedroom_time * 1.5

    # Calculate the total time to renovate the bedrooms and kitchen
    total_bedroom_kitchen_time = (bedroom_time * 3) + kitchen_time

    # Calculate the total time to renovate everything else
    living_room_time = total_bedroom_kitchen_time * 2

    # Calculate the total time to renovate everything
    total_time = total_bedroom_kitchen_time + living_room_time
    result = total_time
    return result

print(solution())