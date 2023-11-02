def solution():
    # Define Sam's earnings per hour and his earnings for the first month
    earnings_per_hour = 10
    earnings_first_month = 200

    # Calculate Sam's earnings for the second month
    earnings_second_month = earnings_first_month + 150

    # Calculate the total earnings for both months
    total_earnings = earnings_first_month + earnings_second_month

    # Calculate the total number of hours Sam spent on tutoring
    total_hours = total_earnings / earnings_per_hour

    result = total_hours
    return result

print(solution())