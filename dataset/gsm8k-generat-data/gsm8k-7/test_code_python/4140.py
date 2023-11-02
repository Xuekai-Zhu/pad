def solution():
    junior_year_points = 260
    senior_year_percent_increase = 0.2  # 20% increase

    # Calculate the number of points Michael scored during his senior year
    senior_year_points = junior_year_points * (1 + senior_year_percent_increase)

    # Calculate the total number of points Michael scored over both years
    total_points = junior_year_points + senior_year_points
    result = total_points
    return result

print(solution())