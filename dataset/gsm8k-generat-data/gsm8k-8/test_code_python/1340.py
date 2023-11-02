def solution():
    # Define maximum riding time
    max_time = 6

    # Calculate total riding time for the two days at maximum time
    max_days_total = max_time * 2

    # Calculate total riding time for the two days at half the maximum time
    half_days_total = max_time * 0.5 * 2

    # Calculate total riding time for the two days at 1.5 hours
    one_half_days_total = 1.5 * 2

    # Calculate total riding time for all 6 days
    total_riding_time = max_days_total + half_days_total + one_half_days_total

    result = total_riding_time
    return result

print(solution())