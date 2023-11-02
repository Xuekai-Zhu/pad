def solution():
    sesame_seed_size = 3.5 # average size in mm
    wood_frog_egg_size_range = [2, 5] # size range in inches
    sesame_seed_size_in_inches = sesame_seed_size / 25.4 # convert mm to inches
    if wood_frog_egg_size_range[0] <= sesame_seed_size_in_inches <= wood_frog_egg_size_range[1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())