def solution():
    """A pad of paper comes with 60 sheets. Evelyn uses a pad of paper writing notes at work every week. She takes Monday and Friday off from work. How many sheets of paper does she use per day at work?"""
    # Define the number of workdays in a week
    WORKDAYS_PER_WEEK = 5

    # Define the number of sheets of paper used per week
    SHEETS_PER_WEEK = 60

    # Calculate the number of sheets of paper used per workday
    sheets_per_day = SHEETS_PER_WEEK / WORKDAYS_PER_WEEK

    # Display the number of sheets of paper used per workday
    result = sheets_per_day
    return result

print(solution())