def solution():
    jenna_distance = 200
    friend_distance = 100
    jenna_speed = 50
    friend_speed = 20
    num_breaks = 2
    break_time = 0.5  # 30 minutes per break, in hours

    # Calculate Jenna's driving time
    jenna_time = jenna_distance / jenna_speed

    # Calculate her friend's driving time
    friend_time = friend_distance / friend_speed

    # Calculate the total driving time
    total_time = jenna_time + friend_time

    # Add in break time
    total_time += num_breaks * break_time

    result = total_time
    return result

print(solution())