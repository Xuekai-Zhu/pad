def solution():
    # Define the time spent on each step
    step1_time = 30
    step2_time = 0.5 * step1_time
    step3_time = step1_time + step2_time

    # Calculate the total time spent learning the steps
    total_time = step1_time + step2_time + step3_time
    result = total_time
    return result

print(solution())