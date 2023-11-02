def solution():
    """Michael scored 260 points during his junior year on the school basketball team. 
    He scored 20% more points during his senior year. How many points did he score during both years?"""
    junior_year_points = 260
    senior_year_increase = 0.2
    senior_year_points = junior_year_points * (1 + senior_year_increase)
    total_points = junior_year_points + senior_year_points
    result = total_points
    return result

print(solution())