def solution():
    # Define the number of pages read per day
    pages_per_weekday = 10
    pages_per_weekend = 20

    # Calculate the total number of pages read in 2 weeks
    days_in_2_weeks = 5 * 2 + 2 * 2 # 5 weekdays and 2 weekends per week
    total_pages_read = days_in_2_weeks * pages_per_weekday + 2 * pages_per_weekend

    result = total_pages_read
    return result

print(solution())