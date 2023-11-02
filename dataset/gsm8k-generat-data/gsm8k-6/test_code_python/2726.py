def solution():
    # Find the score of the word before it was tripled
    original_score = 30 / 3  # the word was played on a triple word score, so the original score is a third of the total score
    # Find the score of the first and third letters
    side_score = 1 * 2  # the first and third letters were each valued at one point apiece
    # Find the score of the middle letter
    middle_score = original_score - side_score
    result = middle_score
    return result

print(solution())