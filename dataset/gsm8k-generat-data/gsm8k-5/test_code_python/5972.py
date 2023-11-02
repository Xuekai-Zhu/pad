def solution():
    grass_stain_time = 4  # It takes 4 minutes to get rid of each grass stain
    marinara_stain_time = 7  # It takes 7 additional minutes to get rid of each marinara stain
    num_grass_stains = 3  # Bill has 3 grass stains
    num_marinara_stains = 1  # Bill has 1 marinara stain

    # Calculate the total soaking time for grass stains
    total_grass_stain_time = num_grass_stains * grass_stain_time

    # Calculate the total soaking time for marinara stains
    total_marinara_stain_time = num_marinara_stains * marinara_stain_time

    # Calculate the total soaking time for all stains
    total_soak_time = total_grass_stain_time + total_marinara_stain_time
    result = total_soak_time
    return result

print(solution())