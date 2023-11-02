def solution():
    # Calculate Milo's speed on his skateboard and on foot
    skateboard_speed = 2 * running_speed
    running_speed = skateboard_speed / 2

    # Calculate the distance that Milo can run in two hours
    distance = running_speed * 2  # Milo runs for 2 hours

    result = distance
    return result

print(solution())