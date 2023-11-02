def solution():
    
    rental_cost = 150
    gallons_of_gas = 8
    cost_per_gallon_of_gas = 3.50
    gas_cost = gallons_of_gas * cost_per_gallon_of_gas
    miles_driven = 320
    cost_per_mile = 0.50
    mileage_cost = miles_driven * cost_per_mile
    total_cost = rental_cost + gas_cost + mileage_cost
    result = total_cost
    return result

print(solution())