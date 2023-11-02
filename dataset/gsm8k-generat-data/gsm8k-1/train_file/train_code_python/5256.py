def solution():
    """A pad of paper comes with 60 sheets. Evelyn uses a pad of paper writing notes at work every week. 
    She takes Monday and Friday off from work. How many sheets of paper does she use per day at work?"""
    sheets_per_pad = 60
    workdays_per_week = 5
    sheets_used_per_week = sheets_per_pad * workdays_per_week
    sheets_used_per_day = sheets_used_per_week / workdays_per_week
    result = sheets_used_per_day
    return result

print(solution())