def solution():
    """Nicki spent the last year running a lot. For the first half of the year, she ran a total of 20 miles per week. For the second half of the year, she increased the mileage to 30 miles per week. How many miles total did she run for the year?"""
    # Define the number of weeks in the year
    weeks_in_year = 52

    # Calculate the total miles run in the first half of the year
    first_half_miles = 20 * (weeks_in_year / 2)

    # Calculate the total miles run in the second half of the year
    second_half_miles = 30 * (weeks_in_year / 2)

    # Calculate the total miles run for the year
    total_miles = first_half_miles + second_half_miles

    # Return the result
    result = total_miles
    return result

print(solution())