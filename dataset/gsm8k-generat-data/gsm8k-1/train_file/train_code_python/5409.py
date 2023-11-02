def solution():
    """James is trying to decide which trail is faster to hike. One trail is 20 miles and mostly downhill, so James can cover it at 5 miles per hour. The other trail is 12 miles, but it's mostly uphill, so James will only be able to cover 3 miles per hour and will have to take an hour break halfway through. How many hours faster is the fastest hike?"""
    downhill_miles = 20
    uphill_miles = 12
    downhill_speed = 5
    uphill_speed = 3
    uphill_time = uphill_miles / uphill_speed + 1  # adding 1 hour for the break
    downhill_time = downhill_miles / downhill_speed
    time_difference = uphill_time - downhill_time
    result = time_difference
    return result

print(solution())