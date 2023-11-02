def solution():
    first_try = 400  # Homer scored 400 points on the first try
    second_try = first_try - 70  # Homer scored 70 points fewer on the second try
    third_try = 2 * second_try  # Homer scored twice the number of points she scored on the second try on the third try

    # Calculate the total number of points Homer scored in all tries
    total_points = first_try + second_try + third_try
    result = total_points
    return result

print(solution())