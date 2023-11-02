def solution():
    """Abel leaves for a vacation destination 1000 miles away driving 50 miles per hour.  An hour later Alice leaves from the same point for the same destination, traveling 40 miles per hour. How much earlier does Abel reach the destination in minutes??"""
    # Calculate the time it takes for Abel to reach the destination
    abel_time = 1000 / 50

    # Calculate the time it takes for Alice to reach the destination
    alice_time = (1000 - 50) / 40

    # Calculate the time difference in minutes
    minutes_early = (abel_time - alice_time) * 60

    # Display the time difference in minutes
    result = minutes_early
    return result

print(solution())