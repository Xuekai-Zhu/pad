def solution():
    tv_price = 1700  # The TV costs $1700
    hourly_wage = 10  # Latia earns $10 per hour
    work_hours_per_week = 30  # Latia works for 30 hours per week

    # Calculate Latia's monthly earnings
    monthly_earnings = hourly_wage * work_hours_per_week * 4  # 4 weeks in a month

    # Calculate the number of hours Latia needs to work to buy the TV
    hours_to_work = (tv_price - monthly_earnings) / hourly_wage
    result = hours_to_work
    return result

print(solution())