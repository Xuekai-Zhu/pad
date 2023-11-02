def solution():
    """Cowboy Mickey and cowgirl Minnie train horses for a living. On average, Mickey mounts six less than twice as many horses per day as does Minnie, while Minnie mounts three more horses per day than there are days in a week. How many horses does Mickey Mount per week?"""
    minnie_mounts = 7 + 3
    mickey_mounts = 2 * minnie_mounts - 6
    mickey_mounts_per_week = mickey_mounts * 7
    result = mickey_mounts_per_week
    return result

print(solution())