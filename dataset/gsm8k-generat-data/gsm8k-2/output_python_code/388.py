def solution():
    """In a northwestern town, it rained 4 inches per day during the first 15 days of November. For the remainder of the month, the average daily rainfall was twice the amount observed during the first 15 days. What is the total amount of rainfall for this town in November, in inches?"""
    first_half_rainfall = 4 * 15
    second_half_rainfall = 4 * 15 * 2
    total_rainfall = first_half_rainfall + second_half_rainfall
    result = total_rainfall
    return result

print(solution())