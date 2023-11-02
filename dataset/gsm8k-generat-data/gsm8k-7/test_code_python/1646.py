def solution():
    num_buses = 9
    num_passengers = 198

    # Calculate the average number of passengers per bus
    avg_passengers_per_bus = num_passengers / num_buses

    # Calculate the number of passengers in 5 buses
    num_passengers_5_buses = avg_passengers_per_bus * 5
    result = num_passengers_5_buses
    return result

print(solution())