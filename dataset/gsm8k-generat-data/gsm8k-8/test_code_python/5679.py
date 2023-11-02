def solution():
    # Define the number of string cheeses needed per week
    total_needed_per_week = (2 * 5) + (1 * 5) # 2 for oldest, 1 for youngest, 5 days per week

    # Calculate the total needed for 4 weeks
    total_needed_for_4_weeks = total_needed_per_week * 4

    # Calculate the number of packages needed
    packages_needed = total_needed_for_4_weeks // 30 + 1  # Round up to the nearest package

    result = packages_needed
    return result

print(solution())