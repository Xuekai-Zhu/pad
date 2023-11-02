def solution():
    """Andrew works in a company that provides a generous vacation allotment: for every 10 days worked, you get 1 vacation day. If last year Andrew worked 300 days and took 5 days off in March and twice as many in September, how many more vacation days can Andrew still take?"""
    # Define the number of days worked and vacation days taken
    days_worked = 300
    march_days_off = 5
    september_days_off = 2 * march_days_off

    # Calculate the total vacation days earned based on days worked
    total_vacation_days = days_worked // 10

    # Subtract the vacation days taken in March and September
    remaining_vacation_days = total_vacation_days - march_days_off/10 - september_days_off/10

    # return the result
    result = remaining_vacation_days
    return result

print(solution())