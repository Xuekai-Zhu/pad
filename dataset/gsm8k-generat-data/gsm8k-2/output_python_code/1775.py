def solution():
    """The teacher told the class that if they averaged at least 75% on their final exam, they could have a pizza party. Everyone took the exam on Monday, except for William, who was allowed to take it on Tuesday. If there are 30 people in the class, and the average before he took the test was a 74%, what score does he have to get to make sure they get to have a pizza party?"""
    class_size = 30
    desired_average = 0.75
    current_average = 0.74
    total_points_needed = class_size * desired_average
    points_already_earned = class_size * current_average
    points_needed_by_William = total_points_needed - points_already_earned
    minimum_score_needed_by_William = (points_needed_by_William / (class_size + 1)) * 100
    result = minimum_score_needed_by_William
    return result

print(solution())