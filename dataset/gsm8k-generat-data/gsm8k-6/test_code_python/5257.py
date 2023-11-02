def solution():
    workdays = 5  # number of workdays in a week
    days_off = 2  # number of days off in a week
    sheets_per_week = 60  # number of sheets in a pad of paper
    sheets_per_day = (sheets_per_week / workdays)  # calculate sheets per day
    result = sheets_per_day
    return result

print(solution())