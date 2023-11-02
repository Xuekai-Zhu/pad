def solution():
    """24 gallons per second of water flows down a waterfall. If you have an empty basin that can hold 260 gallons of water. The basin leaks water at 4 gallons per second. how long would it take to fill the basin with water from the waterfall in seconds?"""
    flow_rate = 24
    basin_capacity = 260
    leak_rate = 4
    effective_flow_rate = flow_rate - leak_rate
    time_to_fill = basin_capacity / effective_flow_rate
    result = time_to_fill
    return result

print(solution())