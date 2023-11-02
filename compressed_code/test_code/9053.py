def solution():
    
    junior_year_points = 260
    senior_year_increase = 0.2
    senior_year_points = junior_year_points * (1 + senior_year_increase)
    total_points = junior_year_points + senior_year_points
    result = total_points
    return result

print(solution())