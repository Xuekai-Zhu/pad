def solution():
    initial_distance = 600
    initial_rate = 50
    desired_time = initial_distance / initial_rate - 4
    desired_rate = initial_distance / desired_time
    result = desired_rate - initial_rate
    return result

print(solution())