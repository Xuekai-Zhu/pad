def solution():
    """Melinda is taking a 1200-mile trip with her family to visit their cousins. How much time will they save if they drive 60 miles an hour instead of 50 miles an hour?"""
    # Calculate the time it would take to drive 1200 miles at 50 mph
    time_50mph = 1200 / 50

    # Calculate the time it would take to drive 1200 miles at 60 mph
    time_60mph = 1200 / 60

    # Calculate the time saved by driving 60 mph instead of 50 mph
    time_saved = time_50mph - time_60mph

    # Display the time saved
    result = time_saved
    return result

print(solution())