def solution():
    # Calculate the time taken to travel 1200 miles at 50 miles per hour
    time_50mph = 1200 / 50

    # Calculate the time taken to travel 1200 miles at 60 miles per hour
    time_60mph = 1200 / 60

    # Calculate the time saved
    time_saved = time_50mph - time_60mph
    result = time_saved
    return result

print(solution())