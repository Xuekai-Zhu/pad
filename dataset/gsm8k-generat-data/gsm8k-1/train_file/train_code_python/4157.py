def solution():
    """Reyna had 20 lamps with seven light bulbs in each lamp. If 1/4 of them have 2 burnt-out light bulbs each, how many light bulbs are working?"""
    total_lamps = 20
    bulbs_per_lamp = 7
    total_bulbs = total_lamps * bulbs_per_lamp
    burnt_out_lamps = total_lamps / 4
    burnt_out_bulbs = burnt_out_lamps * 2
    working_bulbs = total_bulbs - burnt_out_bulbs
    result = working_bulbs
    return result

print(solution())