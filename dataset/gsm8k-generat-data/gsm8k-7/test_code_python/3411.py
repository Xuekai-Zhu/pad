def solution():
    time_to_carry_backpack = 7 * 60 + 23  # convert 7 minutes and 23 seconds to seconds
    time_to_open_door = 73
    time_to_traverse_without_backpack = 5 * 60 + 58  # convert 5 minutes and 58 seconds to seconds

    # Calculate the total time it takes Lara to complete the obstacle course
    total_time = time_to_carry_backpack + time_to_open_door + time_to_traverse_without_backpack
    result = total_time
    return result

print(solution())