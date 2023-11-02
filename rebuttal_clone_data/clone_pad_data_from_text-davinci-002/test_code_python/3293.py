def solution():
    first_test = 80
    second_test = 75
    third_test = 90
    desired_average = 85
    total_points = first_test + second_test + third_test
    needed_points = (4 * desired_average) - total_points
    needed_grade = needed_points / 4
    result = needed_grade
    return result

print(solution())