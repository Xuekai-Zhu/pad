def solution():
    
    starting_amount = 200
    cost_per_trip = 2
    trips_per_month = 4
    months_per_year = 12
    total_cost = cost_per_trip * trips_per_month * months_per_year
    result = starting_amount - total_cost
    return result

print(solution())