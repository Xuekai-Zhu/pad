def solution():
    cost_per_mile = 2.5
    event_distance = 200
    round_trip = 2
    total_miles = event_distance * round_trip
    total_cost = total_miles * cost_per_mile
    result = total_cost
    return result

print(solution())