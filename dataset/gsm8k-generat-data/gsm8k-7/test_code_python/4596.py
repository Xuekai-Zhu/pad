def solution():
    total_points = 265
    quiz_points = 0
    test_points = 0
    homework_points = 0

    # Calculate the number of quiz points by using the given ratio with test points
    test_points = 4 * quiz_points
    quiz_points = total_points // (test_points + 5)
    homework_points = total_points - quiz_points - test_points

    result = homework_points
    return result

print(solution())