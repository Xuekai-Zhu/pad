def solution():
    # Calculate the total time Marcus spends with his dog
    bath_time = 20  # minutes
    blow_dry_time = bath_time / 2  # half as long as the bath
    walk_distance = 3  # miles
    walk_time = walk_distance / 6 * 60  # time in minutes, at a speed of 6 miles per hour
    total_time = bath_time + blow_dry_time + walk_time
    result = total_time
    return result

print(solution())