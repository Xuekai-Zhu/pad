def solution():
    """Ms. Alice can grade 296 papers in 8 hours. How many papers can she grade in 11 hours?"""
    # Define the number of papers graded and the hours worked
    papers_graded = 296
    hours_worked = 8

    # Calculate the rate of grading per hour
    rate_per_hour = papers_graded / hours_worked

    # Calculate the number of papers that can be graded in 11 hours
    papers_graded_in_11_hours = rate_per_hour * 11

    result = round(papers_graded_in_11_hours)
    return result

print(solution())