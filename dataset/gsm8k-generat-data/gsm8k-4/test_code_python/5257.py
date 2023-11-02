def solution():
    """A pad of paper comes with 60 sheets. Evelyn uses a pad of paper writing notes at work every week. She takes Monday and Friday off from work. How many sheets of paper does she use per day at work?"""
    # Define the number of workdays in a week
    workdays = 5

    # Define the number of sheets in a pad of paper
    pad_sheets = 60

    # Calculate the number of sheets used per workday
    sheets_per_day = (pad_sheets / workdays)

    # Return the result
    result = sheets_per_day
    return result

print(solution())