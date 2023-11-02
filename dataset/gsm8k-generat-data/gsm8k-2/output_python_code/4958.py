def solution():
    """Meryll wants to write 35 multiple-choice questions and 15 problem-solving questions for her Chemistry class.
    She already has written 2/5 of the multiple-choice and 1/3 of the problem-solving questions.
    How many more questions does she need to write for both multiple-choice and problem-solving?"""
    multiple_choice_num = 35
    problem_solving_num = 15
    written_mc = 2 / 5 * multiple_choice_num
    written_ps = 1 / 3 * problem_solving_num
    remaining_mc = multiple_choice_num - written_mc
    remaining_ps = problem_solving_num - written_ps
    total_remaining = remaining_mc + remaining_ps
    result = total_remaining
    return result

print(solution())