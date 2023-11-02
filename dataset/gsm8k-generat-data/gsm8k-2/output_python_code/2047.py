def solution():
    """A question and answer forum has 200 members. The average number of answers posted by each member on the forum is three times as many as the number of questions asked. If each user posts an average of 3 questions per hour, calculate the total number of questions and answers posted on the forum by its users in a day."""

    members = 200
    questions_per_member = 3
    answers_per_member = 3 * questions_per_member
    questions_per_hour = 3
    hours_per_day = 24
    total_questions = members * questions_per_member * questions_per_hour * hours_per_day
    total_answers = members * answers_per_member * questions_per_hour * hours_per_day
    result = total_questions + total_answers
    return result

print(solution())