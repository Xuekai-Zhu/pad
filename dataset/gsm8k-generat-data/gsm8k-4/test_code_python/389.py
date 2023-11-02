def solution():
    """In a northwestern town, it rained 4 inches per day during the first 15 days of November. For the remainder of the month, the average daily rainfall was twice the amount observed during the first 15 days. What is the total amount of rainfall for this town in November, in inches?"""
    # Define the number of days in November
    num_days = 30

    # Calculate the rainfall during the first 15 days
    first_15_days = 4 * 15

    # Calculate the average daily rainfall for the rest of the month
    avg_rainfall = 2 * 4

    # Calculate the rainfall for the rest of the month
    remaining_days = num_days - 15
    remaining_rainfall = avg_rainfall * remaining_days

    # Calculate the total rainfall for the month
    total_rainfall = first_15_days + remaining_rainfall

    # return the result
    result = total_rainfall
    return result

print(solution())