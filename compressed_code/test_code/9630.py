def solution():
    
    initial_miles = 1728
    gas_capacity = 20
    miles_per_gallon = 30
    total_gas_used = gas_capacity * 2
    total_miles_driven = total_gas_used * miles_per_gallon
    final_miles = initial_miles + total_miles_driven
    result = final_miles
    return result

print(solution())