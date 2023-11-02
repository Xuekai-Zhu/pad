def solution():
    """Amanda has taken 4 quizzes this semester and averaged a 92% score on them. The final quiz is coming up, which is worth the same as each previous quiz. What score does she need in order to get an A in the class, which requires her to average 93% over the 5 quizzes?"""
    current_avg = 92
    desired_avg = 93
    total_quizzes = 5
    score_needed = (desired_avg * total_quizzes) - (current_avg * (total_quizzes - 1))
    result = score_needed
    return result

print(solution())