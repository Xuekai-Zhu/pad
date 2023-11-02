def solution():
    """Sadie has 140 math homework problems for the week. 40 percent are Algebra problems, and half of the Algebra problems are solving linear equations. How many solving linear equations problems does Sadie have to solve?"""
    # Define the number of total math homework problems
    total_problems = 140

    # Calculate the number of Algebra problems
    algebra_problems = int(total_problems * 0.4)

    # Calculate the number of solving linear equations problems
    linear_problems = int(algebra_problems * 0.5)

    # Display the number of solving linear equations problems
    result = linear_problems
    return result

print(solution())