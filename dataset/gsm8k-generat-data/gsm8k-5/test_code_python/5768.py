def solution():
    num_quizzes = 5  # Amanda will take a total of 5 quizzes
    current_average = 92  # Amanda's current average score on the first 4 quizzes is 92%
    desired_average = 93  # Amanda needs to average 93% over all 5 quizzes to get an A in the class
    final_quiz_weight = 1 / num_quizzes  # Each quiz is worth the same, so the final quiz has a weight of 1/5

    # Calculate the score Amanda needs to get on the final quiz
    required_score = (desired_average - (current_average * final_quiz_weight)) / final_quiz_weight
    result = required_score
    return result

print(solution())