def solution():
    """Jeremy loves to play Scrabble. He once played a three-letter word on a triple word score to earn thirty points. If before the word score was tripled, the first and third letters were each valued at one point apiece, how much was the middle letter valued at before the word score was tripled?"""
    total_score = 30
    score_before_triple = total_score / 3
    value_of_first_and_third_letters = 2
    value_of_middle_letter = score_before_triple - (2 * value_of_first_and_third_letters)
    result = value_of_middle_letter
    return result

print(solution())