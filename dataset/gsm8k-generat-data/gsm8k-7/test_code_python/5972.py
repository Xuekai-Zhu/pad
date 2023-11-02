def solution():
    grass_stain_time = 4
    marinara_stain_time = 7
    num_grass_stains = 3
    num_marinara_stains = 1

    # Calculate the total time needed for grass stains
    grass_time = grass_stain_time * num_grass_stains

    # Calculate the total time needed for marinara stains
    marinara_time = marinara_stain_time * num_marinara_stains

    # Calculate the total time needed to soak the clothes
    total_time = grass_time + marinara_time
    result = total_time
    return result

print(solution())