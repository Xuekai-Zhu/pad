def solution():
    total_average = 94
    third_quiz_score = 92

    # Calculate the sum of the scores for the first two quizzes
    sum_first_two_quizzes = (total_average * 3) - third_quiz_score

    # Calculate the average of the first two quizzes
    average_first_two_quizzes = sum_first_two_quizzes / 2

    result = average_first_two_quizzes
    return result

print(solution())