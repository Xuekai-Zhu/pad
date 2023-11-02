def solution():
    # Calculate the total score after three quizzes
    total_score = 94 * 3

    # Calculate the score after the third quiz
    third_quiz_score = 92

    # Calculate the score after the first two quizzes
    first_two_quizzes_score = total_score - third_quiz_score

    # Calculate the average of the first two quizzes
    average_first_two_quizzes = first_two_quizzes_score / 2

    result = average_first_two_quizzes
    return result

print(solution())