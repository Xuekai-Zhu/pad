def solution():
    
    total_bulbs = 20 * 7
    num_burnt_out_lamps = 20 // 4
    num_burnt_out_bulbs = 2 * num_burnt_out_lamps
    working_bulbs = total_bulbs - num_burnt_out_bulbs
    result = working_bulbs
    return result

print(solution())