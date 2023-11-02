def solution():
    # Calculate the total number of questions answered in the first group
    group_1_questions = 6 * 2  # 6 people, 2 questions each

    # Calculate the total number of questions answered in the second group
    group_2_questions = 11 * 2  # 11 people, 2 questions each

    # Calculate the total number of questions answered in the third group
    group_3_questions = 7 * 2  # 7 people, 2 questions each
    group_3_questions += 3 * 2  # 1 person asked 3 times as many questions, so 3 * 2 = 6 questions total

    # Calculate the total number of questions answered in the fourth group
    group_4_questions = 7 * 2  # 7 people, 2 questions each

    # Calculate the total number of questions answered overall
    total_questions = group_1_questions + group_2_questions + group_3_questions + group_4_questions
    result = total_questions
    return result

print(solution())