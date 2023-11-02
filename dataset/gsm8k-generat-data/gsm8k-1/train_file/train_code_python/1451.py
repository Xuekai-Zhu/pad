def solution():
    """Abel leaves for a vacation destination 1000 miles away driving 50 miles per hour. An hour later Alice leaves from the same point for the same destination, traveling 40 miles per hour. How much earlier does Abel reach the destination in minutes?"""
    distance = 1000
    abel_speed = 50
    alice_speed = 40
    abel_time = distance/abel_speed
    alice_time = distance/alice_speed
    time_difference = abel_time - (alice_time + 1) # Adding 1 hour of difference when Alice starts
    time_difference_minutes = time_difference * 60
    result = time_difference_minutes
    return result

print(solution())