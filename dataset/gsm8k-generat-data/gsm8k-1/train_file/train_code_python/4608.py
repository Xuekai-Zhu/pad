def solution():
    """Lizette scored 92 on her third quiz giving her an average of 94. What is Lizette's average in her first two quizzes?"""
    third_quiz_score = 92
    overall_average = 94
    average_of_first_two_quizzes = (overall_average * 3 - third_quiz_score) / 2
    result = average_of_first_two_quizzes
    return result

print(solution())