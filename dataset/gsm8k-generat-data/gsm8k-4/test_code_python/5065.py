def solution():
    """Angela wants to check her math homework answers with her friends, but some of them aren't done yet. Out of 20 problems, Martha has finished 2, Jenna has finished four times the number Martha did minus 2, and Mark has finished half the number Jenna did. If none of the friends worked on any of the same problems, how many problems have no one but Angela finished?"""
    # Define the total number of problems and the number finished by Martha
    total_problems = 20
    martha_problems = 2

    # Calculate the number finished by Jenna
    jenna_problems = 4*martha_problems - 2

    # Calculate the number finished by Mark
    mark_problems = jenna_problems / 2

    # Calculate the total number of problems finished by Angela's friends
    total_finished = martha_problems + jenna_problems + mark_problems

    # Calculate the number of problems that no one but Angela finished
    angela_problems = total_problems - total_finished

    #return the result
    result = angela_problems
    return result

print(solution())