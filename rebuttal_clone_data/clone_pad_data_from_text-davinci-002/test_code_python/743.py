def solution():
    mileage = 400
    passenger_count = 30
    crew_count = 5
    bags_per_person = 2
    fuel_per_mile_empty = 20
    fuel_per_mile_per_passenger = 3
    fuel_per_mile_per_bag = 2
    total_fuel_needed = (fuel_per_mile_empty
                        + (fuel_per_mile_per_passenger * passenger_count)
                        + (fuel_per_mile_per_bag * (passenger_count * bags_per_person))) * mileage
    result = total_fuel_needed
    
    return result

print(solution())