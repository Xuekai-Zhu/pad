def solution():
    bob_speed = 6 # miles per hour
    jim_speed = 9 # miles per hour
    head_start = 1 # mile

    # Convert speeds to miles per minute
    bob_speed /= 60
    jim_speed /= 60

    # Calculate the time it takes for Jim to catch up to Bob
    time = head_start / (jim_speed - bob_speed)
    time_minutes = time * 60
    result = time_minutes
    return result

print(solution())