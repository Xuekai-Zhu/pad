def solution():
    # Calculate the total time taken to renovate the bedrooms
    bedroom_time = 3 * 4  # each bedroom takes 4 hours

    # Calculate the time taken to renovate the kitchen
    kitchen_time = bedroom_time * 1.5  # kitchen takes 50% longer than a bedroom

    # Calculate the total time taken for the bedrooms and kitchen
    total_time = bedroom_time + kitchen_time

    # Calculate the time taken to renovate the living room
    living_room_time = total_time * 2  # living room takes twice as much time as everything else combined

    # Calculate the total time taken for everything
    total_time = bedroom_time + kitchen_time + living_room_time
    result = total_time
    return result

print(solution())