def solution():
    
    desired_average = 85
    num_students = 10
    current_total = 5 * 92 + 4 * 80
    points_needed = desired_average * num_students - current_total
    result = points_needed
    return result

print(solution())