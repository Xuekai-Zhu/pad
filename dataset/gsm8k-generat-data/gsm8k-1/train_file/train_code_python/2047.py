def solution():
    """A question and answer forum has 200 members. The average number of answers posted by each member on the forum is three times as many as the number of questions asked. If each user posts an average of 3 questions per hour, calculate the total number of questions and answers posted on the forum by its users in a day."""
    members = 200
    questions_per_hour = 3
    hours_per_day = 24

    # Calculate total questions asked in a day
    total_questions = members * questions_per_hour * hours_per_day

    # Calculate average number of answers per question
    answers_per_question = 3

    # Calculate total answers posted in a day
    total_answers = members * total_questions * answers_per_question

    # Calculate total posts in a day
    total_posts = total_questions + total_answers

    result = total_posts
    return result

print(solution())