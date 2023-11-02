def solution():
    num_quizzes = 5
    desired_average = 93
    previous_average = 92

    # Calculate the total score Amanda needs to achieve her desired average
    total_desired_score = num_quizzes * desired_average

    # Calculate the total score she currently has from the previous quizzes
    total_previous_score = num_quizzes * previous_average - previous_average

    # Calculate the score she needs on the final quiz
    final_quiz_score = total_desired_score - total_previous_score

    result = final_quiz_score
    return result

print(solution())