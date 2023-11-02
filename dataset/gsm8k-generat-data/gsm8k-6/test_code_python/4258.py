def solution():
    # Calculate the number of horses Minnie mounts per day
    horses_per_day_min = 7 + 3  # Minnie mounts three more horses per day than there are days in a week

    # Calculate the number of horses Mickey mounts per day
    horses_per_day_mic = 2 * horses_per_day_min - 6  # Mickey mounts six less than twice as many horses per day as does Minnie

    # Calculate the number of horses Mickey mounts per week
    horses_per_week_mic = horses_per_day_mic * 7

    result = horses_per_week_mic
    return result

print(solution())