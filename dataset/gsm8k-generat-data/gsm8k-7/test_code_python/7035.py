def solution():
    num_assignments = 9
    ahmed_grade = 91
    emily_grade = 92
    final_assignment_weight = num_assignments

    # Calculate the total points Ahmed and Emily have before the final assignment
    ahmed_points = ahmed_grade * num_assignments
    emily_points = emily_grade * num_assignments

    # Calculate the total points Emily has after the final assignment
    emily_points += 90 * final_assignment_weight

    # Calculate the minimum grade Ahmed needs to beat Emily
    min_ahmed_grade = (emily_points - ahmed_points) / final_assignment_weight
    result = min_ahmed_grade
    return result

print(solution())