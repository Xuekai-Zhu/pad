def solution():
    """Angela wants to check her math homework answers with her friends, but some of them aren't done yet. Out of 20 problems, Martha has finished 2, Jenna has finished four times the number Martha did minus 2, and Mark has finished half the number Jenna did. If none of the friends worked on any of the same problems, how many problems have no one but Angela finished?"""
    total_problems = 20
    martha_finished = 2
    jenna_finished = 4 * martha_finished - 2
    mark_finished = jenna_finished / 2
    problems_left = total_problems - (martha_finished + jenna_finished + mark_finished + 1) # add 1 for Angela
    result = problems_left
    return result

print(solution())