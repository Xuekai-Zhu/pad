def solution():
    """Jeremy loves to play Scrabble.  He once played a three-letter word on a triple word score to earn thirty points.  If before the word score was tripled, the first and third letters were each valued at one point apiece, how much was the middle letter valued at before the word score was tripled?"""
    # Let x be the value of the middle letter before the word score was tripled
    # The total value of the word before the triple word score is 2 + x + 2 = x + 4
    # After the triple word score, the total score is 30
    # Therefore, 3(x + 4) = 30
    # Solving for x, we get x = 8

    # Display the value of the middle letter before the word score was tripled
    result = 8
    return result

print(solution())