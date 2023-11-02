def solution():
    """Amanda has taken 4 quizzes this semester and averaged a 92% score on them.
    The final quiz is coming up, which is worth the same as each previous quiz.
    What score does she need in order to get an A in the class, which requires her to average 93% over the 5 quizzes?"""
    # Define Amanda's current average score and the number of quizzes she has taken so far
    current_average = 92
    num_quizzes = 4

    # Define the desired average score for an A in the class and the total number of quizzes
    desired_average = 93
    total_quizzes = 5

    # Calculate the minimum score Amanda needs on the final quiz to get an A in the class
    minimum_score = (desired_average * total_quizzes) - (current_average * num_quizzes)

    # Display the minimum score Amanda needs on the final quiz
    result = minimum_score
    return result

print(solution())