def solution():
    """Paul, a biology teacher, assigns 265 points in the first quarter. There are 4 times as many test points as quiz points, and 5 more quiz points than homework points. How many homework points are there in the first quarter?"""
    total_points = 265
    quiz_points = (total_points - 5) / 9
    test_points = quiz_points * 4
    homework_points = total_points - quiz_points - test_points
    result = homework_points
    return result

print(solution())