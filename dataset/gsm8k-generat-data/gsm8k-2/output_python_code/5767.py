def solution():
    """Amanda has taken 4 quizzes this semester and averaged a 92% score on them. The final quiz is coming up, which is worth the same as each previous quiz. What score does she need in order to get an A in the class, which requires her to average 93% over the 5 quizzes?"""
    current_average = 92
    final_weight = 1/5
    desired_average = 93
    # solving for the score needed on the final quiz
    final_score = (desired_average - (current_average * 4 * final_weight))/final_weight
    result = final_score
    return result

print(solution())