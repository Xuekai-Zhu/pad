def solution():
    num_lamps = 20
    num_light_bulbs_per_lamp = 7
    num_burnt_out_lamps = num_lamps / 4
    num_burnt_out_bulbs = num_burnt_out_lamps * 2
    num_working_bulbs = (num_lamps * num_light_bulbs_per_lamp) - num_burnt_out_bulbs
    result = num_working_bulbs
    return result

print(solution())