def solution():
    # Calculate the number of days Randy can practice in a year
    days_practiced = (5 * 52) - (2 * 2)  # 5 days a week for 52 weeks in a year with 2 weeks of vacation
    years_to_practice = 20 - 12  # Randy wants to become an expert before he is 20
    total_practice_days = days_practiced * years_to_practice  # total number of days he can practice before turning 20
    hours_needed_per_day = 10000 / total_practice_days  # calculate the number of hours he needs to practice per day
    result = hours_needed_per_day
    return result

print(solution())