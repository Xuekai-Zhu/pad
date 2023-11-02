def solution():
    # Calculate the total points Carl needs to achieve an 85 average
    total_points_needed = 85 * 4

    # Calculate the total points Carl has already earned
    total_points_earned = 80 + 75 + 90

    # Calculate the minimum grade Carl needs on his last test
    minimum_grade_needed = (total_points_needed - total_points_earned) / 1

    result = minimum_grade_needed
    return result

print(solution())