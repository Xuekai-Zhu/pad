def solution():
    
    car_tolls_per_week = 3*2*12.50
    motorcycle_tolls_per_week = 2*2*7
    total_tolls_per_week = car_tolls_per_week + motorcycle_tolls_per_week
    car_gas_per_week = 3*(14*2/35)*3.75
    motorcycle_gas_per_week = 2*(14*2/35)*3.75
    total_gas_per_week = car_gas_per_week + motorcycle_gas_per_week
    result = total_tolls_per_week + total_gas_per_week
    return result

print(solution())