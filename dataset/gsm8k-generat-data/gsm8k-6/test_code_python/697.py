def solution():
    # Calculate the total number of hours Joey will study over 6 weeks
    weekday_hours = 2 * 5  # 2 hours per night for 5 nights
    weekend_hours = 3 * 2  # 3 hours per day for 2 days
    total_hours = (weekday_hours * 6) + (weekend_hours * 6)  # 6 weeks in total
    result = total_hours
    return result

print(solution())