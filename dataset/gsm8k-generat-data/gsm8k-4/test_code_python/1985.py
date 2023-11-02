def solution():
    """24 gallons per second of water flows down a waterfall. If you have an empty basin that can hold 260 gallons of water. The basin leaks water at 4 gallons per second. how long would it take to fill the basin with water from the waterfall in seconds?"""
    # Define the flow rate of the waterfall and the capacity of the basin
    WATERFALL_FLOW_RATE = 24
    BASIN_CAPACITY = 260

    # Define the leakage rate of the basin
    BASIN_LEAKAGE_RATE = 4

    # Calculate the net flow rate into the basin
    net_flow_rate = WATERFALL_FLOW_RATE - BASIN_LEAKAGE_RATE

    # Calculate the time it would take to fill the basin
    fill_time = (BASIN_CAPACITY / net_flow_rate) * 60

    # return the result in seconds
    result = fill_time
    return result

print(solution())