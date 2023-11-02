def solution():
    """Randy got 90, 98, 92, and 94 in his first four quizzes. His goal is to get a 94 average on his 5 quizzes. What score should he get in the fifth quiz to reach his desired average?"""
    # Define the current scores and the desired average
    current_scores = [90, 98, 92, 94]
    desired_average = 94

    # Calculate the current average
    current_average = sum(current_scores) / len(current_scores)

    # Calculate the score needed to reach the desired average on the fifth quiz
    score_needed = (desired_average * 5) - sum(current_scores)

    # Display the score needed
    result = score_needed
    return result

print(solution())