def solution():
    num_members = 200
    avg_answers_per_question = 3
    avg_questions_per_hour = 3
    hours_per_day = 24

    # Calculate the total number of questions asked by all members in one day
    total_questions = num_members * avg_questions_per_hour * hours_per_day

    # Calculate the total number of answers posted by all members in one day
    total_answers = num_members * avg_answers_per_question * total_questions

    # Calculate the sum of questions and answers
    total_posts = total_questions + total_answers
    result = total_posts
    return result

print(solution())