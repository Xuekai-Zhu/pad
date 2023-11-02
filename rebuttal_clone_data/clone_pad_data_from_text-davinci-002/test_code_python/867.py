def solution():
    bob_speed = 6
    jim_speed = 9
    head_start = 1
    time_to_catch = head_start / (jim_speed - bob_speed)
    result = time_to_catch
    return result

print(solution())