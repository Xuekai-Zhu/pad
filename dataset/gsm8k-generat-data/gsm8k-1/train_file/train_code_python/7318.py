def solution():
    """A train takes 4 hours to reach a destination at a speed of 50 miles per hour. How long would it take if it traveled at 100 miles per hour instead?"""
    distance = 50 * 4  # distance = speed * time
    new_speed = 100
    new_time = distance / new_speed
    result = new_time
    return result

print(solution())