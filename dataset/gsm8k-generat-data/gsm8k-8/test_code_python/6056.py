def solution():
    # Define the arrival times in minutes past 8:00 a.m.
    paul_arrival = 25
    amoura_arrival = paul_arrival + 30
    ingrid_arrival = amoura_arrival + 3 * 30

    # Calculate the total delay in minutes
    total_delay = ingrid_arrival - 8 * 60

    # Return the delay in minutes
    result = total_delay
    return result

print(solution())