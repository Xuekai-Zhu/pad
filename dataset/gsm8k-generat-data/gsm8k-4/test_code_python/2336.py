def solution():
    """Latia wants to buy a Samsung TV worth $1700. She works for a delivery service company for a month earning $10 per hour for a 30-hour workweek. How many more hours does she have to work to buy the TV?"""
    # Define the price of the Samsung TV
    tv_price = 1700

    # Define Latia's hourly wage and weekly work hours
    hourly_wage = 10
    weekly_work_hours = 30

    # Calculate Latia's total earnings in a month
    monthly_earnings = hourly_wage * weekly_work_hours * 4

    # Calculate the remaining amount of money needed to buy the TV
    remaining_money = tv_price - monthly_earnings

    # Calculate the number of additional hours Latia needs to work to earn enough money for the TV
    additional_hours = remaining_money / hourly_wage

    # Round up the number of additional hours to the nearest whole number
    additional_hours = int(round(additional_hours, 0))

    result = additional_hours
    return result

print(solution())