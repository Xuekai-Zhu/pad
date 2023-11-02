def solution():
    """Robi Ney wants to fill a 120-liter tub. He is amused by letting the water run for 1 minute, then closing the water supply for 1 minute, and so on alternating opening and closing the water supply. But the cap at the bottom of the tub is not very airtight and lets 1 liter of water escape per minute. The flow rate of the tap is 12 liters per minute. How long does it take to fill the tub in minutes?"""
    tub_size = 120
    fill_rate = 12
    escape_rate = 1
    time_to_fill = 0
    water_in_tub = 0
    while water_in_tub < tub_size:
        # Fill tub for 1 minute
        water_in_tub += fill_rate
        time_to_fill += 1
        
        # Check if tub is full or needs to be drained due to overflow
        if water_in_tub >= tub_size:
            time_to_fill -= (water_in_tub - tub_size) / fill_rate
            break
        elif water_in_tub > tub_size - escape_rate:
            drain_time = (water_in_tub - tub_size + escape_rate) / escape_rate
            water_in_tub = tub_size
            time_to_fill += drain_time
        
        # Wait for 1 minute
        time_to_fill += 1
    
    result = time_to_fill
    return result

print(solution())