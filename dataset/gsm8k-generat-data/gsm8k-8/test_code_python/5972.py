def solution():
    # Define the time needed to remove each type of stain
    grass_stain_time = 4
    marinara_stain_time = 7

    # Define the number of grass and marinara stains
    num_grass_stains = 3
    num_marinara_stains = 1

    # Calculate the total time needed to soak the clothes
    total_time = (num_grass_stains * grass_stain_time) + (num_marinara_stains * marinara_stain_time)
    result = total_time
    return result

print(solution())