def solution():
    """There are some lions in Londolozi at first. Lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month. If there are 148 lions in Londolozi after 1 year, how many lions were there in Londolozi at first?"""
    # Define the initial number of lions and the number of months in a year
    initial_lions = None
    months_in_year = 12

    # Use a loop to calculate the number of lions each month for a year
    lions = initial_lions
    for month in range(months_in_year):
        lions += 5  # Add the number of cubs born
        lions -= 1  # Subtract the number of lions that die

    # Check if the final number of lions matches the given number
    final_lions = lions
    if final_lions == 148:
        # If the final number of lions matches, calculate the initial number
        initial_lions = final_lions - (5 * months_in_year) + months_in_year
    else:
        # If the final number of lions does not match, return an error message
        initial_lions = "Error: final number of lions does not match given number"
    
    result = initial_lions
    return result

print(solution())