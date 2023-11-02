def solution():
    """Arabella is a dance student learning three new steps this session. Her instructor has her spend thirty minutes on learning the first step. The second step she masters in half the time. The third step is more complex, so it takes her as long as both the other steps to learn. How many minutes did she spend learning the three steps?"""
    first_step_time = 30
    second_step_time = first_step_time / 2
    third_step_time = (first_step_time + second_step_time)
    total_learning_time = first_step_time + second_step_time + third_step_time
    result = total_learning_time
    return result

print(solution())