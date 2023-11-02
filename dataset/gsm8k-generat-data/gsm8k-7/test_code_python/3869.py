def solution():
    ideal_weeknight_sleep = 8
    ideal_weekend_sleep = 8
    current_weeknight_sleep = 5
    current_weekend_sleep = 6

    # Calculate the total hours of sleep Tom should have had on weeknights
    ideal_weeknight_hours = ideal_weeknight_sleep * 5

    # Calculate the total hours of sleep Tom should have had on weekends
    ideal_weekend_hours = ideal_weekend_sleep * 2

    # Calculate the total hours of sleep Tom actually had on weeknights
    current_weeknight_hours = current_weeknight_sleep * 5

    # Calculate the total hours of sleep Tom actually had on weekends
    current_weekend_hours = current_weekend_sleep * 2

    # Calculate the total hours of sleep Tom is behind on
    total_sleep_deficit = (ideal_weeknight_hours + ideal_weekend_hours) - (current_weeknight_hours + current_weekend_hours)

    result = total_sleep_deficit
    return result

print(solution())