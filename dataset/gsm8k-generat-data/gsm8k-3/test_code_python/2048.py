def solution():
    """A question and answer forum has 200 members. The average number of answers posted by each member on the forum is three times as many as the number of questions asked. If each user posts an average of 3 questions per hour, calculate the total number of questions and answers posted on the forum by its users in a day."""
    # Define the number of members on the forum
    members = 200

    # Define the average number of questions asked per user per hour
    questions_per_user_per_hour = 3

    # Define the ratio of answers to questions
    answers_to_questions_ratio = 3

    # Calculate the total number of questions asked per hour
    total_questions_per_hour = members * questions_per_user_per_hour

    # Calculate the total number of answers posted per hour
    total_answers_per_hour = answers_to_questions_ratio * total_questions_per_hour

    # Calculate the total number of questions and answers posted in a day
    total_questions_and_answers_per_day = (total_questions_per_hour + total_answers_per_hour) * 24

    # Display the total number of questions and answers posted in a day
    result = total_questions_and_answers_per_day
    return result

print(solution())