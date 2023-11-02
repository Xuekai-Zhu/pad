def solution():
    """Bill gets paid $20 every hour he works up to a total of 40 hours, after which he gets paid double that amount per hour. How much does Bill get paid for a 50-hour workweek?"""
    # Define the regular hourly rate and the number of hours worked
    regular_rate = 20
    total_hours = 50

    if total_hours <= 40:
        # Calculate the total pay for the first 40 hours worked
        total_pay = total_hours * regular_rate
    else:
        # Calculate the pay for the first 40 hours worked
        first_40_pay = 40 * regular_rate

        # Calculate the pay for the remaining hours at double the regular rate
        extra_hours = total_hours - 40
        extra_pay = extra_hours * (2 * regular_rate)

        # Calculate the total pay
        total_pay = first_40_pay + extra_pay

    # return the result
    result = total_pay
    return result

print(solution())