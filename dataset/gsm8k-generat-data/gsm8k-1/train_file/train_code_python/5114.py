def solution():
    """Janet makes $20 per hour at work. She works 52 hours per week. Anything over 40 hours per week is considered overtime and is paid at 1.5 times the normal rate. She wants to purchase a $4640 car. How many weeks does she need to work to purchase the car?"""
    hourly_rate = 20
    overtime_rate = 1.5 * hourly_rate
    regular_hours = 40
    overtime_hours = 52 - regular_hours
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * overtime_rate
    total_pay = regular_pay + overtime_pay
    weeks_to_purchase = 4640 / total_pay
    result = weeks_to_purchase
    return result

print(solution())