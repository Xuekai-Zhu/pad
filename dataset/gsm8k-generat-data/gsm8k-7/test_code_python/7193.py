def solution():
    highest_score = 100  # assuming the test is out of 100 points
    score_to_beat1 = 95
    score_to_beat2 = (40-3)/40 * 100  # calculate the percentage of correct answers for the student who got 3 wrong
    questions_to_get_right = int(round((highest_score-score_to_beat1)/(highest_score/100), 0))  # round to nearest whole number
    questions_to_get_right2 = int(round((highest_score-score_to_beat2)/(highest_score/100), 0))  # round to nearest whole number
    result = max(questions_to_get_right, questions_to_get_right2)  # choose the higher value of the two
    return result

print(solution())