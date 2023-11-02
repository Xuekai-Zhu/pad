def solution():
    water_flow_rate = 24  # gallons per second
    basin_capacity = 260  # gallons
    leak_rate = 4  # gallons per second

    # Calculate the net water flow rate into the basin
    net_flow_rate = water_flow_rate - leak_rate

    # Calculate the time it takes to fill the basin
    time_to_fill = basin_capacity / net_flow_rate
    result = time_to_fill
    return result

print(solution())