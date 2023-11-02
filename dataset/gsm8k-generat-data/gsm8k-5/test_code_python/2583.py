def solution():
    total_hours = 48  # Cindy teaches for a total of 48 hours per week
    num_courses = 4  # Cindy teaches 4 math courses
    hours_per_course = total_hours / num_courses  # Cindy spends 12 hours in each math course per week

    # Calculate Cindy's earnings for teaching 1 math course in a week
    earnings_per_course_per_week = hours_per_course * 25  # Cindy earns $25 per hour teaching math
    earnings_per_course_per_month = earnings_per_course_per_week * 4  # There are 4 weeks in a month

    result = earnings_per_course_per_month
    return result

print(solution())