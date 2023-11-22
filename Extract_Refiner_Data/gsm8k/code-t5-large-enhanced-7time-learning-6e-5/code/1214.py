def solution():
    
    grades_per_year = 4 * 7
    points_per_student = 10 * 8
    total_points = points_per_student * 10
    time_per_group = 45
    groups = grades_per_year / points_per_student
    total_time = groups * time_per_group
    result = total_time
    return result

print(solution())