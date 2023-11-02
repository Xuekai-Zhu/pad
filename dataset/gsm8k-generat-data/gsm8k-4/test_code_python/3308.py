def solution():
    """Jason worked for 9 years as a bartender and 3 years and six months as a manager. How many months of work experience does he have total?"""
    # Define the number of months in a year
    MONTHS_PER_YEAR = 12

    # Calculate the total number of months worked
    total_months = (9 * MONTHS_PER_YEAR) + (3 * MONTHS_PER_YEAR) + 6

    # return the result
    result = total_months
    return result

print(solution())