def solution():
    # Jeremy earned 30 points for a three-letter word on a triple word score
    total_points = 30
    triple_word_score = 3

    # The first and third letters were each valued at 1 point apiece
    point_value_1 = 1
    point_value_3 = 1

    # Determine the total number of points earned for this three-letter word before the triple word score was applied
    pre_triple_score = (point_value_1 + point_value_3) + (point_value_middle * triple_word_score)

    # Solve for the value of the middle letter
    point_value_middle = (total_points / triple_word_score - pre_triple_score) / triple_word_score

    result = point_value_middle
    return result

print(solution())