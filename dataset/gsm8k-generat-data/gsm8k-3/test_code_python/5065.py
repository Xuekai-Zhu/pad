def solution():
    """Angela wants to check her math homework answers with her friends, but some of them aren't done yet. Out of 20 problems, Martha has finished 2, Jenna has finished four times the number Martha did minus 2, and Mark has finished half the number Jenna did. If none of the friends worked on any of the same problems, how many problems have no one but Angela finished?"""
    # Define the number of problems finished by each friend
    martha_problems = 2
    jenna_problems = 4 * martha_problems - 2
    mark_problems = jenna_problems / 2

    # Calculate the total number of problems finished by all friends
    total_problems = martha_problems + jenna_problems + mark_problems

    # Calculate the number of problems that no one but Angela finished
    no_one_problems = 20 - total_problems

    # Display the number of problems that no one but Angela finished
    result = no_one_problems
    return result

print(solution())