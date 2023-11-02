def solution():
    """Randy got 90, 98, 92, and 94 in his first four quizzes. His goal is to get a 94 average on his 5 quizzes. What score should he get in the fifth quiz to reach his desired average?"""
    # Calculate Randy's current average
    current_average = (90 + 98 + 92 + 94) / 4

    # Calculate the score Randy needs on the fifth quiz to reach his desired average
    desired_average = 94
    fifth_quiz_score = desired_average * 5 - (90 + 98 + 92 + 94)

    # Display the score Randy needs on the fifth quiz
    result = fifth_quiz_score
    return result

print(solution())