def solution():
    """Jimmy needs to score at least 50 points to pass to the next class. He earned 20 points for each of the 3 exams he wrote but lost 5 points during the school year for bad behavior. How many more points can Jimmy lose and still be able to pass the next class?"""
    passing_score = 50
    earned_points = 20 * 3
    lost_points = 5
    total_points = earned_points - lost_points
    remaining_points_needed = passing_score - total_points
    result = remaining_points_needed
    return result

print(solution())