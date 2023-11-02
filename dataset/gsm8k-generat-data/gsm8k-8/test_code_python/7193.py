def solution():
    # Calculate the maximum possible score for the student who got 3 wrong
    max_possible_score = 40 - 3

    # Calculate the score Hannah needs to beat
    score_to_beat = max(95, max_possible_score)

    # Calculate the number of questions Hannah needs to get right to beat the score
    num_questions_to_get_right = round(score_to_beat / 100 * 40)

    result = num_questions_to_get_right
    return result

print(solution())