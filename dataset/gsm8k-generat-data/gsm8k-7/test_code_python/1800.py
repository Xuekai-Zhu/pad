def solution():
    leo_mistakes = 4  # twice as many as Madeline's 2 mistakes
    brent_mistakes = leo_mistakes + 1
    brent_score = 25

    # Calculate Leo's score
    leo_score = brent_score + brent_mistakes

    # Calculate Madeline's score
    madeline_score = leo_score + leo_mistakes - 2
    result = madeline_score
    return result

print(solution())