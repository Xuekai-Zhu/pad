def solution():
    total_problems = 75
    problems_solved = 10
    problems_solved_2 = problems_solved * 2
    problems_remaining = total_problems - (problems_solved + problems_solved_2)
    result =  problems_remaining
    return result

print(solution())