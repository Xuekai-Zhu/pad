def solution():
    
    total_questions = 50
    sylvia_incorrect_answers = total_questions * (1/5)
    sylvia_correct_answers = total_questions - sylvia_incorrect_answers
    sergio_correct_answers = total_questions - 4
    difference = sergio_correct_answers - sylvia_correct_answers
    result = difference
    return result

print(solution())