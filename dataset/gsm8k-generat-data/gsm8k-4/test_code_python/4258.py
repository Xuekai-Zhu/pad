def solution():
    """Cowboy Mickey and cowgirl Minnie train horses for a living. On average, Mickey mounts six less than twice as many horses per day as does Minnie, while Minnie mounts three more horses per day than there are days in a week. How many horses does Mickey Mount per week?"""
    # Define the number of days in a week
    days_in_week = 7

    # Define the number of horses Minnie mounts per day
    minnie_horses_per_day = days_in_week + 3

    # Define the number of horses Mickey mounts per day in terms of Minnie's
    mickey_horses_per_day = 2 * minnie_horses_per_day - 6

    # Calculate the number of horses Mickey mounts per week
    mickey_horses_per_week = mickey_horses_per_day * days_in_week

    # Return the result
    result = mickey_horses_per_week
    return result

print(solution())