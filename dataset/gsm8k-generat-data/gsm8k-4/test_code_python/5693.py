def solution():
    """Kim loves to knit sweaters and can knit as many as 10 sweaters in a day if she gets the time. On a particular week, she knit 8 sweaters on Monday, 2 more sweaters on Tuesday than on Monday, 4 fewer sweaters on both Wednesday and Thursday than on Tuesday, and half the number of sweaters she had knit on Monday on Friday. Calculate the total number of sweaters she knit that week."""
    # Define the number of sweaters knit on Monday
    sweaters_monday = 8

    # Calculate the number of sweaters knit on Tuesday
    sweaters_tuesday = sweaters_monday + 2

    # Calculate the number of sweaters knit on Wednesday and Thursday
    sweaters_wed_thurs = sweaters_tuesday - 4

    # Calculate the number of sweaters knit on Friday
    sweaters_friday = sweaters_monday / 2

    # Calculate the total number of sweaters knit that week
    total_sweaters = sweaters_monday + sweaters_tuesday + sweaters_wed_thurs * 2 + sweaters_friday

    # return the result
    result = total_sweaters
    return result

print(solution())