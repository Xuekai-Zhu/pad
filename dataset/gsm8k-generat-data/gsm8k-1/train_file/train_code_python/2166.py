def solution():
    """A truck driver has to spend $2 per gallon of gas. She can drive 10 miles per gallon. She drives at a rate of 30 miles per hour. If she is paid $.50 per mile, how much money does she make if she drives for 10 hours?"""
    gas_cost_per_gallon = 2
    miles_per_gallon = 10
    rate_of_drive = 30
    miles_per_hour = rate_of_drive * 10
    total_hours = 10
    miles_driven = total_hours * miles_per_hour
    gallons_used = miles_driven / miles_per_gallon
    gas_cost = gallons_used * gas_cost_per_gallon
    pay_per_mile = 0.5
    total_pay = miles_driven * pay_per_mile
    profit = total_pay - gas_cost
    result = profit
    return result

print(solution())