def solution():
    """Jacob takes four tests in his physics class and earns 85, 79, 92 and 84. What must he earn on his fifth and final test to have an overall average of 85?"""
    current_average = (85 + 79 + 92 + 84) / 4
    target_average = 85
    total_points_needed = 5 * target_average - 4 * current_average
    points_needed_on_final_test = total_points_needed
    result = points_needed_on_final_test
    return result

print(solution())