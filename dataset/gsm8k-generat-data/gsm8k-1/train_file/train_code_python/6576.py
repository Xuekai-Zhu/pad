def solution():
    """Jimmy needs to score at least 50 points to pass to the next class. He earned 20 points for each of the 3 exams he wrote but lost 5 points during the school year for bad behavior. How many more points can Jimmy lose and still be able to pass the next class?"""
    exam_points = 60
    behavior_points_lost = 5
    passing_points_required = 50
    points_remaining = passing_points_required - (exam_points - behavior_points_lost)
    result = points_remaining
    return result

print(solution())