def solution():
    """Socorro is preparing for a math contest. She needs to train for a total of 5 hours. Each day, she answers problems about multiplication for 10 minutes and then division problems for 20 minutes. How many days will it take for her to complete her training?"""
    total_training_time = 5 * 60
    multiplication_time = 10
    division_time = 20
    total_problem_time = multiplication_time + division_time
    total_days = total_training_time / total_problem_time
    result = total_days
    return result

print(solution())