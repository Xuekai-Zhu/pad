def solution():
    # Calculate total time taken to walk to work and back 3 times a week
    walking_time = 2 * 3 * 2  # 2 hours to walk to work and back, 3 times a week

    # Calculate total time taken to ride his bike to work and back 2 times a week
    biking_time = 1 * 2 * 2  # 1 hour to ride his bike to work and back, 2 times a week

    # Calculate total time taken to get to and from work a week
    total_time = walking_time + biking_time
    result = total_time
    return result

print(solution())