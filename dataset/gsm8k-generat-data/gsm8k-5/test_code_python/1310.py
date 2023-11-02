def solution():
    total_problems = 45  # Stacy assigned 45 problems for homework

    # Let's use variables to represent the number of each type of problem
    tf_problems = x  # We don't know the number of true/false problems yet
    fr_problems = x + 7  # There are 7 more free response problems than true/false
    mc_problems = 2 * fr_problems  # There are twice as many multiple choice problems as free response

    # Set up an equation using the total number of problems
    equation = tf_problems + fr_problems + mc_problems == total_problems

    # Solve for tf_problems by substituting the expressions for fr_problems and mc_problems
    tf_problems = total_problems - fr_problems - mc_problems
    result = tf_problems
    return result

print(solution())