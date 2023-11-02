def solution():
    """Jacob takes four tests in his physics class and earns 85, 79, 92 and 84. What must he earn on his fifth and final test to have an overall average of 85?"""
    current_average = (85 + 79 + 92 + 84) / 4
    desired_average = 85
    total_points = (desired_average * 5) - (current_average * 4)
    points_needed = total_points - 85
    result = points_needed
    return result

print(solution())