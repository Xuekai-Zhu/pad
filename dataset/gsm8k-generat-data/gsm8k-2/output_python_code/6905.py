def solution():
    """Homer scored 400 points on the first try in a Candy crush game, 70 points fewer on the second try, and twice the number of points she scored on the second try on the third try. What's the total number of points that she scored in all tries?"""
    first_try = 400
    second_try = first_try - 70
    third_try = 2 * second_try
    total_points = first_try + second_try + third_try
    result = total_points
    return result

print(solution())