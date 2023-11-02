def solution():
    num_problems = 20

    # Calculate the number of problems Martha has finished
    martha_problems = 2

    # Calculate the number of problems Jenna has finished
    jenna_problems = (4 * martha_problems) - 2

    # Calculate the number of problems Mark has finished
    mark_problems = jenna_problems / 2

    # Calculate the total number of problems that no one but Angela finished
    num_unfinished_problems = num_problems - (martha_problems + jenna_problems + mark_problems)
    result = num_unfinished_problems
    return result

print(solution())