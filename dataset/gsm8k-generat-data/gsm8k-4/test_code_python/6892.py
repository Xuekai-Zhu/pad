def solution():
    """Sadie has 140 math homework problems for the week. 40 percent are Algebra problems, and half of the Algebra problems are solving linear equations. How many solving linear equations problems does Sadie have to solve?"""
    # Define the total number of math homework problems
    total_problems = 140

    # Calculate the number of algebra problems
    algebra_problems = total_problems * 0.4

    # Calculate the number of linear equation problems within algebra problems
    linear_problems = algebra_problems * 0.5

    # return the result
    result = linear_problems
    return result

print(solution())