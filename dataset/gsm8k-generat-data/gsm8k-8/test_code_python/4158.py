def solution():
    # Calculate the total number of light bulbs
    total_bulbs = 20 * 7

    # Calculate the number of lamps with burnt-out light bulbs
    burnt_out_lamps = int(20 * (1/4))
    
    # Calculate the total number of burnt-out light bulbs
    total_burnt_out = 2 * burnt_out_lamps
    
    # Calculate the number of working light bulbs
    working_bulbs = total_bulbs - total_burnt_out
    result = working_bulbs
    return result

print(solution())