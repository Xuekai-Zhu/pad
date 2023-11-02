def solution():
    # Calculate the total number of hours Cindy worked in a month
    total_hours = 48 * 4

    # Calculate the number of hours Cindy worked per math course
    hours_per_course = total_hours / 4

    # Calculate Cindy's earnings per math course per month
    earnings_per_course = hours_per_course * 25

    result = earnings_per_course
    return result

print(solution())