def solution():
    """Amanda has taken 4 quizzes this semester and averaged a 92% score on them. The final quiz is coming up, which is worth the same as each previous quiz. What score does she need in order to get an A in the class, which requires her to average 93% over the 5 quizzes?"""
    # Define the number of quizzes Amanda has taken and her current average score
    total_quizzes = 5
    current_average = 92

    # Define the weight of each quiz
    quiz_weight = 1 / total_quizzes

    # Define the desired average score and calculate the total weight needed for that score
    desired_average = 93
    needed_weight = desired_average - (current_average * (total_quizzes - 1)) / total_quizzes

    # Calculate the score Amanda needs to get on the final quiz to achieve the desired average
    needed_score = needed_weight / quiz_weight

    # Return the result
    result = needed_score
    return result

print(solution())