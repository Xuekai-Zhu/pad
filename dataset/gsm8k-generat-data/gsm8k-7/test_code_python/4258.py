def solution():
    minnie_mounts = 7 + 3  # Minnie mounts 3 more horses than 7 days in a week
    mickey_mounts = 2 * minnie_mounts - 6  # Mickey mounts 6 less than twice as many horses as Minnie
    mickey_weekly_mounts = 7 * mickey_mounts  # Multiply Mickey's daily mounts by 7 to get weekly mounts
    result = mickey_weekly_mounts
    return result

print(solution())