def solution():
    """Reyna had 20 lamps with seven light bulbs in each lamp. If 1/4 of them have 2 burnt-out light bulbs each, how many light bulbs are working?"""
    total_bulbs = 20 * 7
    num_burnt_out_lamps = 20 // 4
    num_burnt_out_bulbs = 2 * num_burnt_out_lamps
    working_bulbs = total_bulbs - num_burnt_out_bulbs
    result = working_bulbs
    return result

print(solution())