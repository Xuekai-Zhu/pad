def solution():
    total_problems = 140
    algebra_percent = 0.4
    linear_equations_percent = 0.5

    # Calculate the number of Algebra problems
    algebra_problems = total_problems * algebra_percent

    # Calculate the number of solving linear equations problems
    linear_equations_problems = algebra_problems * linear_equations_percent
    result = linear_equations_problems
    return result

print(solution())