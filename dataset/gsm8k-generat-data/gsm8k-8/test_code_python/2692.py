def solution():
    # Define the scores and desired average
    quiz1 = 90
    quiz2 = 98
    quiz3 = 92
    quiz4 = 94
    desired_average = 94

    # Calculate the total sum of the first four quizzes
    sum_first_quizzes = quiz1 + quiz2 + quiz3 + quiz4

    # Calculate the score needed on the fifth quiz to achieve the desired average
    score_needed = (desired_average * 5) - sum_first_quizzes
    result = score_needed
    return result

print(solution())