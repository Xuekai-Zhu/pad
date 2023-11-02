def solution():
    # Define the flow rate and capacity
    flow_rate = 24 # gallons per second
    basin_capacity = 260 # gallons

    # Define the leakage rate
    leakage_rate = 4 # gallons per second

    # Determine the net flow rate
    net_flow_rate = flow_rate - leakage_rate

    # Determine the time to fill the basin
    time_to_fill = basin_capacity / net_flow_rate
    result = time_to_fill
    return result

print(solution())