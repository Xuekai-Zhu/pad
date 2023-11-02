def solution():
    """Jeremy loves to play Scrabble. He once played a three-letter word on a triple word score to earn thirty points. If before the word score was tripled, the first and third letters were each valued at one point apiece, how much was the middle letter valued at before the word score was tripled?"""
    # Define the score of the first and third letters
    first_score = 1
    third_score = 1

    # Define the total score of the word after being tripled
    triple_score = 30 / 3

    # Calculate the score of the middle letter
    middle_score = (triple_score - first_score - third_score)

    # Display the score of the middle letter
    result = middle_score
    return result

print(solution())