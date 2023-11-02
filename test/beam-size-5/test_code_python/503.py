def solution():
    num_bus_trips_per_week = 2
    cost_per_bus_trip = 2.20
    num_days_per_week = 5
    num_bus_trips_per_week = num_bus_trips_per_week * num_days_per_week

    # Calculate the total cost of buying a weekly bus pass
    total_cost = num_bus_trips_per_week * cost_per_bus_trip

    # Calculate the amount saved by buying a weekly bus pass
    amount_saved = total_cost - 20
    result = amount_saved
    return result

print(solution())