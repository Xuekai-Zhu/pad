def solution():
    # Define the number of problems each friend finished
    martha_finished = 2
    jenna_finished = 4 * martha_finished - 2
    mark_finished = 0.5 * jenna_finished

    # Calculate the total number of problems finished by Angela's friends
    total_finished = martha_finished + jenna_finished + mark_finished

    # Calculate the number of problems that no one but Angela finished
    total_problems = 20
    no_one_finished = total_problems - total_finished
    result = no_one_finished
    return result

print(solution())