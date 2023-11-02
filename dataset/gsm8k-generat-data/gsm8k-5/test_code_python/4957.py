def solution():
    initial_speed = 70  # Jan's initial speed was 70 skips per minute
    new_speed = initial_speed * 2  # Jan doubles her speed after training
    duration = 5  # Jan skips for 5 minutes

    # Calculate the total number of skips Jan does in 5 minutes at her new speed
    total_skips = new_speed * duration
    result = total_skips
    return result

print(solution())