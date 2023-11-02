def solution():
    total_points = 265
    quiz_points = x
    homework_points = x - 5
    test_points = 4 * quiz_points

    # Equation 1: total_points = quiz_points + homework_points + test_points
    # Equation 2: test_points = 4 * quiz_points
    # Substituting Equation 2 into Equation 1:
    # total_points = quiz_points + homework_points + 4 * quiz_points
    # total_points = 5 * quiz_points + homework_points

    # Solving for quiz_points
    quiz_points = (total_points - homework_points) / 5

    result = x - 5 # since homework_points = quiz_points - 5
    return result

print(solution())