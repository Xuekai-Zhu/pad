def solution():
    """Homer scored 400 points on the first try in a Candy crush game, 70 points fewer on the second try, and twice the number of points she scored on the second try on the third try. What's the total number of points that she scored in all tries?"""
    first_try_score = 400
    second_try_score = first_try_score - 70
    third_try_score = second_try_score * 2
    total_score = first_try_score + second_try_score + third_try_score
    result = total_score
    return result

print(solution())