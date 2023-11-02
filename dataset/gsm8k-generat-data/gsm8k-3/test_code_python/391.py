def solution():
    """In a northwestern town, it rained 4 inches per day during the first 15 days of November.  For the remainder of the month, the average daily rainfall was twice the amount observed during the first 15 days.  What is the total amount of rainfall for this town in November, in inches?"""
    # Define the rainfall per day during the first 15 days
    FIRST_HALF_RAINFALL = 4

    # Define the number of days in November
    NOVEMBER_DAYS = 30

    # Calculate the rainfall for the first half of November
    first_half_rainfall = FIRST_HALF_RAINFALL * 15

    # Calculate the average daily rainfall for the second half of November
    second_half_rainfall = FIRST_HALF_RAINFALL * 2

    # Calculate the rainfall for the second half of November
    second_half_rainfall = second_half_rainfall * (NOVEMBER_DAYS - 15)

    # Calculate the total rainfall for November
    total_rainfall = first_half_rainfall + second_half_rainfall

    # Display the total rainfall
    result = total_rainfall
    return result

print(solution())