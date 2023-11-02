def solution():
    """Janet makes $20 per hour at work. She works 52 hours per week. Anything over 40 hours per week is considered overtime and is paid at 1.5 times the normal rate. She wants to purchase a $4640 car. How many weeks does she need to work to purchase the car?"""
    # Define the hourly wage and the number of regular and overtime hours worked per week
    hourly_wage = 20
    regular_hours = 40
    overtime_hours = 12

    # Calculate the weekly earnings
    regular_earnings = regular_hours * hourly_wage
    overtime_earnings = overtime_hours * hourly_wage * 1.5
    weekly_earnings = regular_earnings + overtime_earnings

    # Calculate the number of weeks needed to purchase the car
    car_price = 4640
    weeks_to_purchase = car_price / weekly_earnings

    # Return the result
    result = weeks_to_purchase
    return result

print(solution())