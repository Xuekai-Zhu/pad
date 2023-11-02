def solution():
    # Calculate the total number of questions posted by all members in a day
    questions_per_member = 3  # each user posts an average of 3 questions per hour
    total_questions = questions_per_member * 200 * 24  # 200 members, 24 hours in a day

    # Calculate the total number of answers posted by all members in a day
    answers_per_member = 3 * questions_per_member  # average number of answers posted is three times the number of questions asked
    total_answers = answers_per_member * 200 * 24  # 200 members, 24 hours in a day

    result = total_questions + total_answers
    return result

print(solution())