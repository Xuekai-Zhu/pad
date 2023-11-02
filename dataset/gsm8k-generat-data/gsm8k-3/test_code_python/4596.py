def solution():
    """Paul, a biology teacher, assigns 265 points in the first quarter.  There are 4 times as many test points as quiz points, and 5 more quiz points than homework points.  How many homework points are there in the first quarter?"""
    # Define the number of test, quiz, and homework points
    test_points = 4
    quiz_points = 1
    homework_points = 1

    # Calculate the total number of quiz points
    quiz_points_total = quiz_points + 5

    # Calculate the total number of test points
    test_points_total = test_points * quiz_points_total

    # Calculate the total number of points
    total_points = test_points_total + quiz_points_total + homework_points

    # Calculate the number of homework points
    homework_points_total = 265 / total_points * homework_points

    # Display the number of homework points
    result = homework_points_total
    return result

print(solution())