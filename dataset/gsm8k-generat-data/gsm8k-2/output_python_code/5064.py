def solution():
    """Angela wants to check her math homework answers with her friends, but some of them aren't done yet. Out of 20 problems, Martha has finished 2, Jenna has finished four times the number Martha did minus 2, and Mark has finished half the number Jenna did. If none of the friends worked on any of the same problems, how many problems have no one but Angela finished?"""
    total_problems = 20
    martha_problems = 2
    jenna_problems = (4 * martha_problems) - 2
    mark_problems = jenna_problems / 2
    angela_problems = total_problems - (martha_problems + jenna_problems + mark_problems)
    result = angela_problems
    return result

print(solution())