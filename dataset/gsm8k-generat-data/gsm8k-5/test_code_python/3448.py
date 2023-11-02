def solution():
    total_towels = 18
    towels_per_day = 2
    missed_weeks = 1

    # Calculate the number of towels used in the missed week
    missed_towels = towels_per_day * 7 * missed_weeks

    # Calculate the number of towels available after the missed week
    available_towels = total_towels - missed_towels

    # Calculate the number of days without clean towels
    days_without_clean_towels = available_towels // towels_per_day
    result = days_without_clean_towels
    return result

print(solution())