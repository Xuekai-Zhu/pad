def solution():
    # Define the amount of water needed to put out the fire
    water_needed = 4000
    
    # Define the flow rate of one firefighter's hose
    flow_rate = 20
    
    # Calculate the total flow rate of the team of 5 firefighters
    total_flow_rate = flow_rate * 5
    
    # Calculate the time needed to deliver the required amount of water
    time_needed = water_needed / total_flow_rate
    result = time_needed
    return result

print(solution())