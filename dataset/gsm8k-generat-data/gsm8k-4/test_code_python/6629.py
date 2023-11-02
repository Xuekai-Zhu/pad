def solution():
    """Cameron guides tour groups in a museum. He usually answers two questions per tourist. Today, he did four tours. The early morning first group was only 6 people. The following group was a busy group of 11. The third group had 8 people, but one was inquisitive and asked three times as many questions as usual. The last group of the day was a late group of 7. How many questions did Cameron answer?"""
    # Calculate the number of questions for the first group
    group_one = 6 * 2

    # Calculate the number of questions for the second group
    group_two = 11 * 2

    # Calculate the number of questions for the third group, accounting for the inquisitive tourist
    group_three = (8-1) * 2 + 3 * 2

    # Calculate the number of questions for the fourth group
    group_four = 7 * 2

    # Calculate the total number of questions answered
    total_questions = group_one + group_two + group_three + group_four

    # return the result
    result = total_questions
    return result

print(solution())