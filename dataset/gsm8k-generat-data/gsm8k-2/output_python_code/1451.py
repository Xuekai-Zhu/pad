def solution():
    """Abel leaves for a vacation destination 1000 miles away driving 50 miles per hour. An hour later Alice leaves from the same point for the same destination, traveling 40 miles per hour. How much earlier does Abel reach the destination in minutes?"""
    distance = 1000
    abel_speed = 50
    alice_speed = 40
    abel_time = distance / abel_speed
    alice_time = distance / alice_speed
    difference_in_time = abel_time - (alice_time + 1)
    difference_in_minutes = difference_in_time * 60
    result = difference_in_minutes
    return result

print(solution())