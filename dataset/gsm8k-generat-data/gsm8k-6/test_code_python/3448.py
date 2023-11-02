def solution():
    # Calculate the total number of clean towels that Barney needs for the week
    clean_towels_needed = 2 * 7  # uses 2 towels a day for 7 days
    total_towels = 18  # total number of towels he owns
    missed_laundry_weeks = 1  # number of weeks he missed doing laundry
    clean_towels_missed = clean_towels_needed - (total_towels - 2)  # towels he didn't have due to missed laundry week

    # Calculate the number of days he won't have clean towels the following week
    missed_days = clean_towels_missed // 2  # he uses 2 towels a day
    result = missed_days
    return result

print(solution())