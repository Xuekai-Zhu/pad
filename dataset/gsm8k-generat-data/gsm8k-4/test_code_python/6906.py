def solution():
    """Homer scored 400 points on the first try in a Candy crush game, 70 points fewer on the second try, and twice the number of points she scored on the second try on the third try. What's the total number of points that she scored in all tries?"""
    # Define the score in the first try
    score_1 = 400

    # Calculate the score in the second try
    score_2 = score_1 - 70

    # Calculate the score in the third try
    score_3 = score_2 * 2

    # Calculate the total score
    total_score = score_1 + score_2 + score_3

    # return the result
    result = total_score
    return result

print(solution())