def solution():
    total_problems = 20
    martha_problems = 2
    jenna_problems = 4 * martha_problems - 2
    mark_problems = jenna_problems / 2

    # Calculate the total number of problems finished by Angela's friends
    total_finished = martha_problems + jenna_problems + mark_problems

    # Calculate the number of problems that no one but Angela finished
    uncompleted_problems = total_problems - total_finished
    result = uncompleted_problems
    return result

print(solution())