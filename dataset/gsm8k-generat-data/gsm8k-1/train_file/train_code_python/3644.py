def solution():
    """Geordie takes a toll road on his drive to work and back every day of his five-day workweek. The toll is $12.50 per car or $7 per motorcycle. Both his car and his motorcycle get 35 miles per gallon of gas and the commute to work is 14 miles. Gas costs him $3.75 per gallon. Geordie drives his car to work three times a week and his motorcycle to work twice a week. How many dollars does he spend driving to work and back on the same route in a week?"""
    car_tolls_per_week = 3*2*12.50
    motorcycle_tolls_per_week = 2*2*7
    total_tolls_per_week = car_tolls_per_week + motorcycle_tolls_per_week
    car_gas_per_week = 3*(14*2/35)*3.75
    motorcycle_gas_per_week = 2*(14*2/35)*3.75
    total_gas_per_week = car_gas_per_week + motorcycle_gas_per_week
    result = total_tolls_per_week + total_gas_per_week
    return result

print(solution())