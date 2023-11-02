def solution():
    quiz_scores = [90, 98, 92, 94]
    desired_average = 94
    num_quizzes = 5

    # Calculate the total score Randy needs to get for all 5 quizzes
    total_desired_score = desired_average * num_quizzes

    # Calculate Randy's current total score
    current_total_score = sum(quiz_scores)

    # Calculate the score Randy needs to get on the fifth quiz
    score_on_fifth_quiz = total_desired_score - current_total_score

    result = score_on_fifth_quiz
    return result

print(solution())