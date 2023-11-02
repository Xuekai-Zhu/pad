def solution():
    
    cattle = 400
    truck_capacity = 20
    miles_to_travel = 60
    hours_to_travel = miles_to_travel / 60
    trips_required = cattle / truck_capacity
    total_hours = hours_to_travel * trips_required
    result = total_hours
    return result

print(solution())