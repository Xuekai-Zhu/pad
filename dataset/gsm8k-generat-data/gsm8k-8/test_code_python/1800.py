def solution():
    # Define Leo's number of mistakes
    leo_mistakes = 4

    # Define Madeline's number of mistakes
    madeline_mistakes = 2

    # Calculate Brent's number of mistakes
    brent_mistakes = leo_mistakes + 1

    # Calculate Madeline's score
    madeline_score = 100 - (madeline_mistakes / 2) * 5

    result = madeline_score
    return result

print(solution())