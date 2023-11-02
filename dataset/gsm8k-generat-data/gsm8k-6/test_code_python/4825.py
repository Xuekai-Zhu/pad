def solution():
    # Calculate the total time Arabella spent learning the three steps
    time_first_step = 30  # minutes spent on learning the first step
    time_second_step = time_first_step / 2  # time spent on learning the second step, half the time spent on the first step
    time_third_step = time_first_step + time_second_step  # time spent on learning the third step, same as the total time spent on the first two steps
    total_time = time_first_step + time_second_step + time_third_step  # total time spent on all three steps
    result = total_time
    return result

print(solution())