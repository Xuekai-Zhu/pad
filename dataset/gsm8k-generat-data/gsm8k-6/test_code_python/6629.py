def solution():
    # Calculate the total number of questions answered by Cameron
    total_questions = 2*(6+11+8) + 2*(3*(1)) + 2*(7)  # first 3 groups had 2 questions per tourist, third group had one tourist with 3 questions, last group had 2 questions per tourist
    result = total_questions
    return result

print(solution())