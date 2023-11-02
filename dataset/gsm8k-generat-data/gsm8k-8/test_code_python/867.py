def solution():
    bob_speed = 6 #miles per hour
    jim_speed = 9 #miles per hour
    head_start = 1 #mile

    # Calculate the time it takes for Jim to catch up to Bob
    time = head_start / (jim_speed - bob_speed) * 60 #convert to minutes

    result = time
    return result

print(solution())