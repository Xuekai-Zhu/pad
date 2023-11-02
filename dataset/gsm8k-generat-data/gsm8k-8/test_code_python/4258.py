def solution():
    # Define the number of days in a week
    days_in_week = 7

    # Calculate the number of horses Minnie mounts per day
    minnie_horses_per_day = days_in_week + 3

    # Calculate the number of horses Mickey mounts per day
    mickey_horses_per_day = (2 * minnie_horses_per_day) - 6

    # Calculate the number of horses Mickey mounts per week
    mickey_horses_per_week = mickey_horses_per_day * days_in_week
    result = mickey_horses_per_week
    return result

print(solution())