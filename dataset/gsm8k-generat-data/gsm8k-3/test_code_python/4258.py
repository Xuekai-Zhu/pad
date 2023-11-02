def solution():
    """Cowboy Mickey and cowgirl Minnie train horses for a living.  On average, Mickey mounts six less than twice as many horses per day as does Minnie,  while Minnie mounts three more horses per day than there are days in a week.  How many horses does Mickey Mount per week?"""
    # Calculate the number of horses Minnie mounts per day
    minnie_horses_per_day = 7 + 3

    # Calculate the number of horses Mickey mounts per day
    mickey_horses_per_day = 2 * minnie_horses_per_day - 6

    # Calculate the number of horses Mickey mounts per week
    mickey_horses_per_week = 7 * mickey_horses_per_day

    # Display the number of horses Mickey mounts per week
    result = mickey_horses_per_week
    return result

print(solution())