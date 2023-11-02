def solution():
    total_problems = 20
    martha_finished = 2
    jenna_finished = 4 * martha_finished - 2
    mark_finished = jenna_finished / 2
    problems_finished = martha_finished + jenna_finished + mark_finished
    problems_not_finished = total_problems - problems_finished
    result = problems_not_finished
    return result

print(solution())