def solution():
    # Calculate the effective water flow rate into the basin
    effective_flow_rate = 24 - 4  # water flows in at 24 gallons/second and leaks out at 4 gallons/second
    # Calculate the time taken to fill the basin
    time_to_fill = 260 / effective_flow_rate
    result = time_to_fill
    return result

print(solution())