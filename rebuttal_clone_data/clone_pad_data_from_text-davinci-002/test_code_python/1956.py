def solution():
    minutes_per_problem_with_calculator = 2
    minutes_per_problem_without_calculator = 5
    number_of_problems = 20
    time_saved = (minutes_per_problem_without_calculator - minutes_per_problem_with_calculator) * number_of_problems
    result = time_saved
    return result

print(solution())