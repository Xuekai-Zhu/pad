def solution():
    """Cindy was hired to teach 4 math courses which required her to be in the classroom for 48 hours a week altogether. How much did Cindy earn for teaching 1 math course in a month with exactly 4 weeks if her hourly rate per class is $25?"""
    # Calculate the total number of hours Cindy spent teaching math courses in a month
    hours_per_week = 48
    weeks_per_month = 4
    total_hours = hours_per_week * weeks_per_month

    # Calculate the number of hours Cindy spent teaching each math course
    hours_per_course = total_hours / 4

    # Calculate Cindy's earnings per math course per month
    hourly_rate = 25
    earnings_per_course = hours_per_course * hourly_rate

    # Return Cindy's earnings per math course per month
    result = earnings_per_course
    return result

print(solution())