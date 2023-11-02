def solution():
    """James is trying to decide which trail is faster to hike. One trail is 20 miles and mostly downhill, so James can cover it at 5 miles per hour. The other trail is 12 miles, but it's mostly uphill, so James will only be able to cover 3 miles per hour and will have to take an hour break halfway through. How many hours faster is the fastest hike?"""
    downhill_distance = 20
    downhill_speed = 5
    uphill_distance = 12
    uphill_speed = 3
    uphill_break_time = 1
    downhill_time = downhill_distance / downhill_speed
    uphill_time = uphill_distance / uphill_speed + uphill_break_time
    faster_time = min(downhill_time, uphill_time)
    slower_time = max(downhill_time, uphill_time)
    time_difference = slower_time - faster_time
    result = time_difference
    return result

print(solution())