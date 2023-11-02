def solution():
    total_floors = 9  # Starting from the 9th floor
    stairs_per_floor = 30  # There are 30 stairs per floor

    # Calculate the total number of stairs Jake needs to descend
    total_stairs = total_floors * stairs_per_floor

    # Calculate the time Jake needs to descend the stairs
    jake_time = total_stairs // 3  # Jake takes 3 steps every second

    # Calculate the time Austin needs to reach the ground floor
    austin_time = 60  # The elevator takes 1 minute to get to ground level

    # Calculate how many seconds later Jake will get to the ground floor
    time_difference = jake_time - austin_time
    result = time_difference
    return result

print(solution())