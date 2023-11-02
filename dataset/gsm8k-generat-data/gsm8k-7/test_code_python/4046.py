def solution():
    hourly_rate = 10
    first_month_earnings = 200
    second_month_earnings = first_month_earnings + 150

    # Calculate the total earnings for both months
    total_earnings = first_month_earnings + second_month_earnings

    # Calculate the total hours spent on tutoring
    total_hours = total_earnings / hourly_rate
    result = total_hours
    return result

print(solution())