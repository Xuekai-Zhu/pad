def solution():
    """Josh works 8 hours a day, 5 days a week, 4 weeks a month. Carl is an intern and works 2 hours less than Josh every day. Josh gets $9 an hour and Carl, half that. How much does the company pay for the 2 together in one month?"""
    # Define the number of hours Josh works
    josh_hours = 8

    # Define the number of hours Carl works
    carl_hours = josh_hours - 2

    # Define the number of days worked in a week and month
    days_per_week = 5
    weeks_per_month = 4

    # Define the hourly rates of Josh and Carl
    josh_rate = 9
    carl_rate = 0.5 * josh_rate

    # Calculate the total number of hours worked by both
    total_hours = (josh_hours + carl_hours) * days_per_week * weeks_per_month

    # Calculate the total pay for Josh and Carl
    josh_pay = josh_rate * josh_hours * days_per_week * weeks_per_month
    carl_pay = carl_rate * carl_hours * days_per_week * weeks_per_month
    total_pay = josh_pay + carl_pay

    # Display the total pay for both workers
    result = total_pay
    return result

print(solution())