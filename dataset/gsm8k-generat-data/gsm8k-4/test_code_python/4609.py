def solution():
    """Lizette scored 92 on her third quiz giving her an average of 94. What is Lizette's average in her first two quizzes?"""
    # Define the total number of quizzes taken so far
    total_quizzes = 3

    # Define the current average
    current_average = 94

    # Define the score on the third quiz
    third_quiz_score = 92

    # Calculate the total score on the first two quizzes
    total_first_two_scores = current_average * (total_quizzes - 1) - third_quiz_score

    # Calculate the average of the first two quizzes
    average_first_two_scores = total_first_two_scores / (total_quizzes - 2)

    # return the result
    result = average_first_two_scores
    return result

print(solution())