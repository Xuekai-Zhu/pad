def solution():
    car_1_mpg = 50
    car_2_mpg = 10
    car_3_mpg = 15
    monthly_mileage = 450
    gas_price = 2
    car_1_gas_usage = monthly_mileage / car_1_mpg
    car_2_gas_usage = monthly_mileage / car_2_mpg
    car_3_gas_usage = monthly_mileage / car_3_mpg
    total_gas_usage = car_1_gas_usage + car_2_gas_usage + car_3_gas_usage
    monthly_gas_cost = total_gas_usage * gas_price
    result = monthly_gas_cost
    
    return result

print(solution())