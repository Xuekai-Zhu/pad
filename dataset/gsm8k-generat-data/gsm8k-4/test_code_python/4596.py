def solution():
    """Paul, a biology teacher, assigns 265 points in the first quarter. There are 4 times as many test points as quiz points, and 5 more quiz points than homework points. How many homework points are there in the first quarter?"""
    # Define the number of quiz points
    quiz_points = None

    # Define the number of test points and the number of homework points
    test_points = None
    homework_points = None

    # Set up an equation in terms of quiz points
    # test points = 4 * quiz points
    # quiz points = homework points + 5
    # total points = quiz points + test points + homework points = 265
    # Use substitution to solve for quiz points, then test points, then homework points
    quiz_points = (265 - 5) / 5
    test_points = 4 * quiz_points
    homework_points = 265 - quiz_points - test_points

    result = homework_points
    return result

print(solution())