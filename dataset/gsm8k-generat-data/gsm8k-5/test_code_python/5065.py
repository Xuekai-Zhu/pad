def solution():
    total_problems = 20  # There are 20 problems in total
    martha_finished = 2  # Martha finished 2 problems
    jenna_finished = (4 * martha_finished) - 2  # Jenna finished 4 times the number Martha did minus 2
    mark_finished = jenna_finished / 2  # Mark finished half the number Jenna did

    # Calculate the total number of problems finished by all three friends
    total_finished = martha_finished + jenna_finished + mark_finished

    # Calculate the number of problems that no one but Angela finished
    problems_unfinished = total_problems - total_finished - 1  # Subtracting 1 for Angela's finished problems

    result = problems_unfinished
    return result

print(solution())