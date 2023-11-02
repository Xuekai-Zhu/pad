def solution():
    
    total_questions = 50
    marks_per_question = 2
    jose_wrong_questions = 5
    jose_question_score = (total_questions - jose_wrong_questions) * marks_per_question
    alisson_question_score = jose_question_score - 40
    meghan_question_score = jose_question_score - 20
    total_score = jose_question_score + alisson_question_score + meghan_question_score
    result = total_score
    return result

print(solution())