def solution():
    # Calculate the number of hours Ludwig works in a week
    hours_per_day = 12  # half a day is 6 hours
    hours_per_week = (4 * hours_per_day) + (3 * 8)  # working 7 days a week, with 3 full days and 4 half days
    # Calculate Ludwig's weekly earnings
    daily_salary = 10
    weekly_earnings = hours_per_week * (daily_salary / 2)  # Ludwig works half a day on Fri, Sat, and Sun
    result = weekly_earnings
    return result

print(solution())