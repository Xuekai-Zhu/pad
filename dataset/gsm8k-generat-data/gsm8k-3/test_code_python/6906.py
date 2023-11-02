def solution():
    """Homer scored 400 points on the first try in a Candy crush game, 70 points fewer on the second try, and twice the number of points she scored on the second try on the third try. What's the total number of points that she scored in all tries?"""
    # Define the number of points scored on the first try
    first_try = 400

    # Define the number of points scored on the second try
    second_try = first_try - 70

    # Define the number of points scored on the third try
    third_try = 2 * second_try

    # Calculate the total number of points scored in all tries
    total_points = first_try + second_try + third_try

    # Display the total number of points
    result = total_points
    return result

print(solution())