def solution():
    time_step1 = 30  # 30 minutes for step 1

    time_step2 = time_step1 / 2  # Half the time for step 2

    time_step3 = time_step1 + time_step2  # Same time as both other steps for step 3

    total_time = time_step1 + time_step2 + time_step3  # Add up all the times

    result = total_time
    return result

print(solution())