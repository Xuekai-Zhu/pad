def solution():
    """In a northwestern town, it rained 4 inches per day during the first 15 days of November. For the remainder of the month, the average daily rainfall was twice the amount observed during the first 15 days. What is the total amount of rainfall for this town in November, in inches?"""
    first_half_days = 15
    second_half_days = 30 - first_half_days
    first_half_rain = 4
    second_half_rain = first_half_rain * 2
    total_rain = (first_half_days * first_half_rain) + (second_half_days * second_half_rain)
    result = total_rain
    return result

print(solution())