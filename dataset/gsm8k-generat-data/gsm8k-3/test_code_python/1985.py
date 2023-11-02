def solution():
    """24 gallons per second of water flows down a waterfall. If you have an empty basin that can hold 260 gallons of water. The basin leaks water at 4 gallons per second. how long would it take to fill the basin with water from the waterfall in seconds?"""
    # Define the variables
    flow_rate = 24 # gallons per second
    basin_capacity = 260 # gallons
    leak_rate = 4 # gallons per second
    time = (basin_capacity - (basin_capacity * (leak_rate/flow_rate))) / flow_rate

    # Display the time in seconds
    result = time
    return result

print(solution())