def solution():
    # Amanda's current average score
    current_average = 92

    # The total score needed to average 93 over 5 quizzes
    total_needed = 93 * 5

    # The total score Amanda has currently earned
    current_total = current_average * 4

    # The score Amanda needs to earn on the final quiz
    final_score_needed = total_needed - current_total

    # Dividing by the weight of each quiz to get the score on the final quiz
    final_quiz_score = final_score_needed / 1

    result = final_quiz_score
    return result

print(solution())