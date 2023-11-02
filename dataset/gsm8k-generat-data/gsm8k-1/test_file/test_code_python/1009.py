def solution():
    """Janet gets a job as a waitress. She makes $10 an hour from wages and another $15 an hour from tips. She wants to save up 20% of the cost of a $10000 car for a downpayment. If she works 40 hours a week how many weeks will she need to work to save the down payment?"""
    wage_per_hour = 10
    tip_per_hour = 15
    total_per_hour = wage_per_hour + tip_per_hour
    cost_of_car = 10000
    down_payment_percent = 20
    down_payment = cost_of_car * (down_payment_percent / 100)
    hours_needed = down_payment / total_per_hour
    weeks_needed = hours_needed / 40
    result = weeks_needed
    return result

print(solution())