def solution():
    sheets_per_pad = 60
    days_per_week = 5  # assuming she only works from Monday to Friday

    # Calculate the total number of sheets she uses in a week
    total_sheets = sheets_per_pad * (days_per_week - 2)

    # Calculate the number of sheets she uses per day at work
    sheets_per_day = total_sheets / days_per_week
    result = sheets_per_day
    return result

print(solution())