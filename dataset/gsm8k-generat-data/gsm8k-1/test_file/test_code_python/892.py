def solution():
    """John rents his car out 10 times a month for 3 hours each time. He gets paid $25 an hour. If his car payment is $500, how much profit does he make on his car?"""
    times_rented_per_month = 10
    hours_rented_per_time = 3
    hourly_rate = 25
    car_payment = 500
    revenue = times_rented_per_month * hours_rented_per_time * hourly_rate
    profit = revenue - car_payment
    result = profit
    return result

print(solution())