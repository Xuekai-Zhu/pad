def solution():
    distance = 50 * 4  # distance = speed * time
    new_speed = 100  # new speed in miles per hour

    # Calculate the new time taken to travel the same distance at the new speed
    new_time = distance / new_speed

    result = new_time
    return result

print(solution())