def solution():
    total_points = 265  # Paul assigns 265 points in the first quarter
    quiz_points = x  # Let the number of quiz points be x
    test_points = 4 * quiz_points  # There are 4 times as many test points as quiz points
    homework_points = quiz_points - 5  # There are 5 more quiz points than homework points
    # The total number of points is the sum of quiz points, test points, and homework points
    equation = quiz_points + test_points + homework_points - total_points

    # Solve for homework points
    homework_points = sympy.symbols('homework_points')
    solution = sympy.solve(equation, homework_points)
    result = solution[0]
    return result

print(solution())