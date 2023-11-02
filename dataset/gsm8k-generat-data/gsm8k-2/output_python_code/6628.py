def solution():
    """Cameron guides tour groups in a museum. He usually answers two questions per tourist. Today, he did four tours. The early morning first group was only 6 people. The following group was a busy group of 11. The third group had 8 people, but one was inquisitive and asked three times as many questions as usual. The last group of the day was a late group of 7. How many questions did Cameron answer?"""
    total_tourists = 6 + 11 + 8 + 7
    group_three_questions = (8 - 1) * 2 + (3 * 2)
    total_questions = total_tourists * 2 + group_three_questions
    result = total_questions
    return result

print(solution())