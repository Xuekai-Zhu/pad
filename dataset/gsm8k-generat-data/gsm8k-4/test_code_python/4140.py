def solution():
    """Michael scored 260 points during his junior year on the school basketball team. He scored 20% more points during his senior year. How many points did he score during both years?"""
    # Define the number of points scored during the junior year
    junior_year_points = 260

    # Calculate the number of points scored during the senior year
    senior_year_points = junior_year_points * 1.2

    # Calculate the total number of points scored during both years
    total_points = junior_year_points + senior_year_points

    # Return the result
    result = total_points
    return result

print(solution())