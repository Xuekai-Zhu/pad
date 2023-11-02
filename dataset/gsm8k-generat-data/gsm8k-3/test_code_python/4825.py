def solution():
    """Arabella is a dance student learning three new steps this session. Her instructor has her spend thirty minutes on learning the first step. The second step she masters in half the time. The third step is more complex, so it takes her as long as both the other steps to learn. How many minutes did she spend learning the three steps?"""
    # Define the time spent on learning the first step
    step1_time = 30

    # Calculate the time spent on learning the second step
    step2_time = step1_time / 2

    # Calculate the time spent on learning the third step
    step3_time = step1_time + step2_time

    # Calculate the total time spent on learning the three steps
    total_time = step1_time + step2_time + step3_time

    # Display the total time
    result = total_time
    return result

print(solution())