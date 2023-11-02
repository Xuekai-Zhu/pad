def solution():
    """Bob is 75 miles ahead of Tom, driving 55 miles per hour. Tom is driving 70 miles per hour. How long will it take Tom to catch up with Bob?"""
    distance_apart = 75
    bob_speed = 55
    tom_speed = 70
    relative_speed = tom_speed - bob_speed
    time_to_catch_up = distance_apart / relative_speed
    result = time_to_catch_up
    return result

print(solution())