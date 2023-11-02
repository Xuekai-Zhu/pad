def solution():
    first_month_earnings = 200  # Sam earned $200 in the first month
    second_month_earnings = first_month_earnings + 150  # Sam earned $150 more in the second month than the first
    hourly_rate = 10  # Sam earns $10 per hour

    # Calculate the total number of hours Sam spent on tutoring for two months
    total_hours = (first_month_earnings + second_month_earnings) / hourly_rate
    result = total_hours
    return result

print(solution())