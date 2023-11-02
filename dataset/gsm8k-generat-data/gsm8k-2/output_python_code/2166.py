def solution():
    """A truck driver has to spend $2 per gallon of gas. She can drive 10 miles per gallon. 
    She drives at a rate of 30 miles per hour. If she is paid $.50 per mile, how much money does she make if she drives for 10 hours?"""
    
    gas_price = 2
    miles_per_gallon = 10
    miles_per_hour = 30
    dollars_per_mile = 0.5
    time_in_hours = 10
    
    gallons_consumed = (miles_per_hour * time_in_hours) / miles_per_gallon
    cost_of_gas = gallons_consumed * gas_price
    total_earnings = miles_per_hour * time_in_hours * dollars_per_mile
    net_profit = total_earnings - cost_of_gas
    
    result = net_profit
    return result

print(solution())