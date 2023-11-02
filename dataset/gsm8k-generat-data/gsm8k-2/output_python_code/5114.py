def solution():
    """Janet makes $20 per hour at work. She works 52 hours per week. Anything over 40 hours per week is considered overtime and is paid at 1.5 times the normal rate. She wants to purchase a $4640 car. How many weeks does she need to work to purchase the car?"""
    normal_rate = 20
    overtime_rate = 1.5 * normal_rate
    regular_hours = 40
    overtime_hours = 52 - regular_hours
    weekly_pay = (normal_rate * regular_hours) + (overtime_rate * overtime_hours)
    car_price = 4640
    weeks_to_purchase = car_price / weekly_pay
    result = weeks_to_purchase
    return result

print(solution())