def solution():
    
    total_lamps = 20
    bulbs_per_lamp = 7
    total_bulbs = total_lamps * bulbs_per_lamp
    burnt_out_lamps = total_lamps / 4
    burnt_out_bulbs = burnt_out_lamps * 2
    working_bulbs = total_bulbs - burnt_out_bulbs
    result = working_bulbs
    return result

print(solution())