def solution():
    
    
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