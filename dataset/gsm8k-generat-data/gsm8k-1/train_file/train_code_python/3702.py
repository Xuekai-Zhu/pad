def solution():
    """Jason is planning a parking garage that will have 12 floors. Every 3rd floor has a gate where drivers have to show ID, which takes two minutes. To get from one floor to the next, drivers have to drive 800 feet at 10 feet/second. How long, in seconds, does it take to get to the bottom of the garage from the top?"""
    num_floors = 12
    gate_floors = [i for i in range(num_floors) if (i+1) % 3 == 0]
    
    # time to go through each gate
    gate_time = 2*len(gate_floors)
    
    # time to drive between floors
    floor_drive_time = 800/10  # seconds
    
    # total time
    total_time = (num_floors-1)*floor_drive_time + gate_time
    
    return total_time

print(solution())