def solution():
    """In 6 months Bella and Bob will be celebrating their 4th anniversary. How many months ago did they celebrate their 2nd anniversary?"""
    # Define the total number of months in 4 years
    total_months = 48

    # Calculate the number of months passed in 4 years at the current moment
    current_months = total_months - 6

    # Calculate the number of months passed in 2 years
    previous_months = total_months - 24

    # Calculate the number of months between their 2nd and 4th anniversaries
    months_between = current_months - previous_months

    # Calculate the number of months ago they celebrated their 2nd anniversary
    months_ago = months_between - 24

    # Return the result
    result = months_ago
    return result

print(solution())