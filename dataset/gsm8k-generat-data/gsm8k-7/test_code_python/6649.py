def solution():
    steps_per_km = 5350 / 3  # calculate the steps per kilometer
    distance_covered = 2.5 * 3  # calculate the total distance covered
    steps_covered = distance_covered * steps_per_km  # calculate the steps covered
    result = steps_covered
    return result

print(solution())