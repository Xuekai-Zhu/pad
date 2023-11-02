def solution():
    """Jeremy loves to play Scrabble. He once played a three-letter word on a triple word score to earn thirty points. If before the word score was tripled, the first and third letters were each valued at one point apiece, how much was the middle letter valued at before the word score was tripled?"""
    total_score = 30 / 3  # Score before the triple word score
    first_and_third = 2  # Value of the first and third letters combined
    middle_value = (total_score - first_and_third) / 1  # Value of the middle letter
    result = middle_value
    return result

print(solution())