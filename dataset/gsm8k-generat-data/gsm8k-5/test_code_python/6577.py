def solution():
    points_per_exam = 20  # Jimmy earned 20 points for each of the 3 exams
    total_exam_points = points_per_exam * 3  # Total points earned from exams
    behavior_points_lost = 5  # Jimmy lost 5 points for bad behavior
    total_points = total_exam_points - behavior_points_lost  # Total points Jimmy has earned
    required_points = 50  # Jimmy needs at least 50 points to pass

    # Calculate the maximum number of points Jimmy can lose and still pass
    max_points_lost = total_points - required_points
    result = max_points_lost
    return result

print(solution())