def solution():
    """Geordie takes a toll road on his drive to work and back every day of his five-day workweek. The toll is $12.50 per car or $7 per motorcycle. Both his car and his motorcycle get 35 miles per gallon of gas and the commute to work is 14 miles. Gas costs him $3.75 per gallon. Geordie drives his car to work three times a week and his motorcycle to work twice a week. How many dollars does he spend driving to work and back on the same route in a week?"""
    car_commute_distance = 14 * 2
    motorcycle_commute_distance = 14 * 2
    car_gas_usage = car_commute_distance / 35
    motorcycle_gas_usage = motorcycle_commute_distance / 35
    car_days_per_week = 3
    motorcycle_days_per_week = 2
    car_toll_cost = 12.5
    motorcycle_toll_cost = 7
    gas_cost = 3.75
    total_car_cost = (car_gas_usage * gas_cost * car_days_per_week) + (car_toll_cost * car_days_per_week)
    total_motorcycle_cost = (motorcycle_gas_usage * gas_cost * motorcycle_days_per_week) + (motorcycle_toll_cost * motorcycle_days_per_week)
    result = total_car_cost + total_motorcycle_cost
    return result

print(solution())