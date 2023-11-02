def solution():
    bob_speed = 6  # Bob runs at 6 miles per hour
    jim_speed = 9  # Jim runs at 9 miles per hour
    head_start = 1  # Bob has a 1 mile head-start

    # Calculate the time it takes for Jim to catch up to Bob
    time_to_catch_up = head_start / (jim_speed - bob_speed) * 60

    result = time_to_catch_up
    return result

print(solution())