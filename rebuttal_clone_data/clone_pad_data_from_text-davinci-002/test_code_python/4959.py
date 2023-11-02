def solution():
    total_multiple_choice = 35
    total_problem_solving = 15
    written_multiple_choice = 2/5 * total_multiple_choice
    written_problem_solving = 1/3 * total_problem_solving
    needed_multiple_choice = total_multiple_choice - written_multiple_choice
    needed_problem_solving = total_problem_solving - written_problem_solving
    result = [needed_multiple_choice, needed_problem_solving]
    return result

print(solution())