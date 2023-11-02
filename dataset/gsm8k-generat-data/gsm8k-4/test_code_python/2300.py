def solution():
    """Josh works 8 hours a day, 5 days a week, 4 weeks a month. Carl is an intern and works 2 hours less than Josh every day. Josh gets $9 an hour and Carl, half that. How much does the company pay for the 2 together in one month?"""
    # Define the number of hours Josh works in a month
    josh_hours = 8 * 5 * 4

    # Calculate Josh's monthly earnings
    josh_earnings = josh_hours * 9

    # Calculate Carl's number of hours and earnings
    carl_hours = josh_hours - 2
    carl_earnings = carl_hours * 4.5

    # Calculate the total earnings for both Josh and Carl
    total_earnings = josh_earnings + carl_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())