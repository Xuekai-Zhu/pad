def solution():
    sheets_per_pad = 60  # A pad of paper comes with 60 sheets
    days_per_week = 5  # Evelyn works 5 days a week (Monday to Friday)
    days_off = 2  # Evelyn takes 2 days off (Monday and Friday)

    # Calculate the total number of sheets used in a week
    sheets_per_week = sheets_per_pad * (days_per_week / 7)

    # Calculate the number of sheets used per day at work
    sheets_per_day = sheets_per_week / (days_per_week - days_off)
    result = sheets_per_day
    return result

print(solution())