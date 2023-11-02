def solution():
    
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