def solution():
    # Define the number of workdays in a week
    workdays = 5

    # Define the number of days off
    days_off = 2

    # Calculate the number of workdays in a year
    workdays_per_year = workdays * 52

    # Calculate the total number of sheets used in a year
    total_sheets_used = workdays_per_year * 1  # As she uses one pad per year

    # Calculate the number of sheets used per workday
    sheets_per_day = total_sheets_used / (workdays_per_year - days_off)

    result = sheets_per_day
    return result

print(solution())