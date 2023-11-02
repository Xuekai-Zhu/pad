def solution():
    """Bill needs to soak his clothes for 4 minutes to get rid of each grass stain and 7 additional minutes to get rid of each marinara stain. If his clothes have 3 grass stains and 1 marinara stain, how long does he need to soak them?"""
    grass_stain_time = 4
    marinara_stain_time = 7
    total_grass_stain_time = grass_stain_time * 3
    total_marinara_stain_time = marinara_stain_time * 1
    total_soak_time = total_grass_stain_time + total_marinara_stain_time
    result = total_soak_time
    return result

print(solution())