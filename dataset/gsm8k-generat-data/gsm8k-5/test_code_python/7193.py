def solution():
    max_score = 100  # The maximum score that can be obtained on the test
    score_to_beat_1 = 95  # The score obtained by the highest scoring student
    score_to_beat_2 = (40-3)/40 * 100  # The score obtained by the student with only 3 wrong answers

    # Calculate the minimum score Hannah needs to obtain to have the highest score in the class
    required_score = max(max_score, score_to_beat_1, score_to_beat_2) + 1
    num_questions_to_get_right = (required_score / 100) * 40  # Calculate the number of questions Hannah needs to get right
    result = num_questions_to_get_right
    return result

print(solution())