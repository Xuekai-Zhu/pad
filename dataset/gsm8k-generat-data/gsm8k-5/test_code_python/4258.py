def solution():
    minnie_mounts = 7 + 3  # Minnie mounts 3 more horses than the days in a week
    mickey_mounts = 2 * minnie_mounts - 6  # Mickey mounts 6 less than twice as many horses as Minnie

    # Calculate the number of horses Mickey mounts per week
    mickey_mounts_per_week = mickey_mounts * 7
    result = mickey_mounts_per_week
    return result

print(solution())