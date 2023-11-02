def solution():
    first_step_time = 30  # Arabella spends 30 minutes on the first step
    second_step_time = first_step_time / 2  # Arabella masters the second step in half the time
    third_step_time = (first_step_time + second_step_time)  # The third step takes as long as both the other steps combined
    total_time = first_step_time + second_step_time + third_step_time  # Calculate the total time

    result = total_time  
    return result

print(solution())