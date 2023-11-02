def solution():
    """A question and answer forum has 200 members. The average number of answers posted by each member on the forum
    is three times as many as the number of questions asked. If each user posts an average of 3 questions per hour, 
    calculate the total number of questions and answers posted on the forum by its users in a day."""
    
    # Define the number of members and the average number of answers per member
    num_members = 200
    avg_answers_per_member = 3 * avg_questions_per_member = 3 * 3 = 9

    # Calculate the total number of questions asked per hour
    total_questions_per_hour = num_members * 3 = 600

    # Calculate the total number of answers posted per hour
    total_answers_per_hour = num_members * avg_answers_per_member = 1800

    # Calculate the total number of questions and answers posted in a day
    total_questions_per_day = total_questions_per_hour * 24 = 14400
    total_answers_per_day = total_answers_per_hour * 24 = 43200

    # Return the total number of questions and answers posted in a day
    result = total_questions_per_day + total_answers_per_day
    return result

print(solution())