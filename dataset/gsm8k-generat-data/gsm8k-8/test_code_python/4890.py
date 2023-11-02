def solution():
    starting_miles = 1728
    gas_tank_capacity = 20
    miles_per_gallon = 30
    
    # Calculate the total miles driven on the trip
    total_miles_driven = (2 * gas_tank_capacity * miles_per_gallon) + starting_miles
    
    result = total_miles_driven
    return result

print(solution())