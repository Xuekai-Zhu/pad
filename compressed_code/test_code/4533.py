def solution():
    
    miles_per_month = 450
    car1_mpg = 50
    car2_mpg = 10
    car3_mpg = 15
    total_gallons_used = (miles_per_month / 3) / car1_mpg + (miles_per_month / 3) / car2_mpg + (miles_per_month / 3) / car3_mpg
    gas_price = 2
    total_gas_cost = total_gallons_used * gas_price
    result = total_gas_cost
    return result

print(solution())