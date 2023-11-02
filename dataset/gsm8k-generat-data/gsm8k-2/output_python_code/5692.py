def solution():
    """Kim loves to knit sweaters and can knit as many as 10 sweaters in a day if she gets the time. On a particular week, she knit 8 sweaters on Monday, 2 more sweaters on Tuesday than on Monday, 4 fewer sweaters on both Wednesday and Thursday than on Tuesday, and half the number of sweaters she had knit on Monday on Friday. Calculate the total number of sweaters she knit that week."""
    monday_sweaters = 8
    tuesday_sweaters = monday_sweaters + 2
    wednesday_sweaters = tuesday_sweaters - 4
    thursday_sweaters = wednesday_sweaters
    friday_sweaters = monday_sweaters / 2
    total_sweaters = monday_sweaters + tuesday_sweaters + wednesday_sweaters + thursday_sweaters + friday_sweaters
    result = total_sweaters
    return result

print(solution())