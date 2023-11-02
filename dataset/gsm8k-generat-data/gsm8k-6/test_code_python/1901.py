def solution():
    total_distance = 200
    distance_covered = total_distance * (1/4)  # distance covered in the first leg of the journey
    time_taken = 1  # time taken for the first leg of the journey
    remaining_distance = total_distance - distance_covered  # remaining distance to be covered
    time_taken += 1  # time taken for lunch break
    # calculate the time taken to cover remaining distance at the same speed as before
    time_remaining = remaining_distance * (1/distance_covered)
    total_time = time_taken + time_remaining
    result = total_time
    return result

print(solution())