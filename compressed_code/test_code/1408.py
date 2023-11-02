def solution():
    
    quiz_scores = [91, 90, 92]
    total_score = sum(quiz_scores)
    num_quizzes = len(quiz_scores)
    average_score = total_score / num_quizzes
    result = average_score
    return result

print(solution())