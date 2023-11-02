def solution():
    # Calculate the total time spent in minutes
    total_minutes = 5 * 60  # 5 hours in minutes

    # Calculate the total time spent on multiplication and division problems
    multiplication_time = 10
    division_time = 20
    total_problem_time = multiplication_time + division_time

    # Calculate the number of problem sets Socorro can complete
    problem_sets = total_minutes // total_problem_time

    # Calculate the number of days needed to complete the training
    days_needed = problem_sets // 2  # assuming she alternates between multiplication and division problems each day

    result = days_needed
    return result

print(solution())