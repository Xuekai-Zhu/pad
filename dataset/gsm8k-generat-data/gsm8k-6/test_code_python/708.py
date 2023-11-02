def solution():
    # Calculate the net flow rate of water into the tub
    net_flow_rate = 12 - 1  # the flow rate of water from the tap is 12 liters per minute and 1 liter of water leaks out per minute

    # Calculate the time taken to fill the tub
    # Each cycle of opening and closing the tap takes 2 minutes, with 1 minute of water flowing and 1 minute of no water flow
    # Each cycle adds a net flow of 11 liters (12 liters minus 1 liter of leakage)
    # Therefore, the time taken to fill the tub can be calculated as follows:
    time_taken = 120 / (11/2)

    result = time_taken
    return result

print(solution())