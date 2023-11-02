def solution():
    num_members = 200
    avg_answers_per_member = 3
    avg_questions_per_member = avg_answers_per_member / 3
    avg_questions_per_hour = 3
    num_hours_in_day = 24
    total_questions = num_members * avg_questions_per_member * num_hours_in_day
    total_answers = num_members * avg_answers_per_member * num_hours_in_day
    result = total_questions + total_answers
    return result

print(solution())