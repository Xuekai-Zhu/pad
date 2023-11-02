def solution():
    # Convert 2 hours to minutes
    time_in_minutes = 2 * 60

    # Calculate how many 5-minute intervals are in 2 hours
    intervals = time_in_minutes // 5

    # Calculate how many oysters can be shucked in those intervals
    oysters = intervals * 10

    result = oysters
    return result

print(solution())