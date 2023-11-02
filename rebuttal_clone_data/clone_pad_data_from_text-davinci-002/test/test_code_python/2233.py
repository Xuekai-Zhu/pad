def solution():
    initial_height = 50
    initial_speed = 40
    trial_run_one = 36
    trial_run_two = 34
    trial_run_three = 38
    average_speed = (trial_run_one + trial_run_two + trial_run_three) / 3
    required_speed = initial_speed - average_speed
    result = required_speed
    return result

print(solution())