def solution():
    """Kim loves to knit sweaters and can knit as many as 10 sweaters in a day if she gets the time. On a particular week, she knit 8 sweaters on Monday, 2 more sweaters on Tuesday than on Monday, 4 fewer sweaters on both Wednesday and Thursday than on Tuesday, and half the number of sweaters she had knit on Monday on Friday. Calculate the total number of sweaters she knit that week."""
    # Define the maximum number of sweaters Kim can knit in a day
    MAX_SWEATERS_PER_DAY = 10

    # Calculate the number of sweaters Kim knits each day of the week
    monday = 8
    tuesday = monday + 2
    wednesday = tuesday - 4
    thursday = wednesday
    friday = monday / 2

    # Calculate the total number of sweaters Kim knit that week
    total_sweaters = monday + tuesday + wednesday + thursday + friday

    # Display the total number of sweaters Kim knit that week
    result = total_sweaters
    return result

print(solution())