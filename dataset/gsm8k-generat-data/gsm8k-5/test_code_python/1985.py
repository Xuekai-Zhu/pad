def solution():
    water_flow_rate = 24  # Gallons per second
    basin_capacity = 260  # Gallons
    leak_rate = 4  # Gallons per second

    # Net water filling rate
    net_fill_rate = water_flow_rate - leak_rate

    # Time to fill the basin
    time_to_fill = (basin_capacity / net_fill_rate) * 3600  # In seconds, 3600 seconds in an hour

    result = time_to_fill
    return result

print(solution())