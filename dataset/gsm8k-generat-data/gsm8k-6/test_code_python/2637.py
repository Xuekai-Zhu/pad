def solution():
    # Calculate the total number of hours needed to sew all 5 dresses
    total_hours = 5 * 12  # Sheena can sew one dress in 12 hours, and there are 5 bridesmaids
    hours_per_week = 4  # Sheena can sew for 4 hours each week
    weeks_needed = total_hours / hours_per_week

    result = weeks_needed
    return result

print(solution())