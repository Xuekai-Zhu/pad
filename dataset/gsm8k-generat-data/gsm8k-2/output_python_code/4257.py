def solution():
    """Cowboy Mickey and cowgirl Minnie train horses for a living. On average, Mickey mounts six less than twice as many horses per day as does Minnie, while Minnie mounts three more horses per day than there are days in a week. How many horses does Mickey Mount per week?"""
    days_in_week = 7
    minnie_horses_per_day = days_in_week + 3
    mickey_horses_per_day = (2*minnie_horses_per_day) - 6
    mickey_horses_per_week = mickey_horses_per_day * days_in_week
    result = mickey_horses_per_week
    return result

print(solution())