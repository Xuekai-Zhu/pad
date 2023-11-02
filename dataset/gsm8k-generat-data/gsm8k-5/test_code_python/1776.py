def solution():
    num_students = 30
    desired_avg = 75
    current_avg = 74
    total_points_needed = num_students * desired_avg
    total_points_before_William = current_avg * (num_students - 1)

    # William needs to get this many points to bring the class average up to desired_avg
    points_needed = total_points_needed - total_points_before_William

    # William needs to get this score to ensure the class has a pizza party
    required_score = (points_needed / num_students) * 100
    result = required_score
    return result

print(solution())