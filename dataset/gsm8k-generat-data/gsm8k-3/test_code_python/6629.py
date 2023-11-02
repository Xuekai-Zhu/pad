def solution():
    """Cameron guides tour groups in a museum. He usually answers two questions per tourist. Today,
    he did four tours. The early morning first group was only 6 people. The following group was a busy group of 11.
    The third group had 8 people, but one was inquisitive and asked three times as many questions as usual.
    The last group of the day was a late group of 7. How many questions did Cameron answer?"""

    # Define the number of people and questions for each group
    group1_people = 6
    group1_questions = group1_people * 2

    group2_people = 11
    group2_questions = group2_people * 2

    group3_people = 8
    group3_questions = (group3_people - 1) * 2 + (group3_people - 1) * 2 * 3

    group4_people = 7
    group4_questions = group4_people * 2

    # Calculate the total number of questions answered
    total_questions = group1_questions + group2_questions + group3_questions + group4_questions

    # Display the total number of questions answered
    result = total_questions
    return result

print(solution())