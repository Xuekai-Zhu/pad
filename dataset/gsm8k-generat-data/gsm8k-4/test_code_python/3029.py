def solution():
    """Mr. Roper cuts his lawn 15 days a month beginning in April and ending in September. From October to the end of March he cuts his lawn three times a month. What is the average number of times that Mr. Roper cuts his yard per month?"""
    # Define the number of months in a year
    MONTHS_IN_YEAR = 12

    # Define the number of months Mr. Roper cuts his lawn between April and September
    APRIL_TO_SEPTEMBER_MONTHS = 6

    # Define the number of times Mr. Roper cuts his lawn between April and September
    APRIL_TO_SEPTEMBER_CUTS = 15 * APRIL_TO_SEPTEMBER_MONTHS

    # Define the number of times Mr. Roper cuts his lawn between October and March
    OCTOBER_TO_MARCH_CUTS = 3 * (MONTHS_IN_YEAR - APRIL_TO_SEPTEMBER_MONTHS)

    # Calculate the total number of lawn cuts in a year
    total_cuts = APRIL_TO_SEPTEMBER_CUTS + OCTOBER_TO_MARCH_CUTS

    # Calculate the average number of cuts per month
    average_cuts_per_month = total_cuts / MONTHS_IN_YEAR

    # return the result
    result = average_cuts_per_month
    return result

print(solution())