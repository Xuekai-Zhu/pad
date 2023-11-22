def solution():
    
    trucks = 20
    tons_per_truck = 20
    total_trucks = trucks * tons_per_truck
    total_time = 2 * 60  # convert 2 hours to minutes
    mechanical_failures = total_trucks * 0.25
    total_lorries = total_trucks + total_time - mechanical_failures
    result = total_lorries
    return result

print(solution())