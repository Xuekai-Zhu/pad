def solution():
    """Bill needs to soak his clothes for 4 minutes to get rid of each grass stain and 7 additional minutes to get rid of each marinara stain. If his clothes have 3 grass stains and 1 marinara stain, how long does he need to soak them?"""
    # Define the time to soak for each type of stain
    GRASS_SOAK_TIME = 4
    MARINARA_SOAK_TIME = 7

    # Define the number of each type of stain
    grass_stains = 3
    marinara_stains = 1

    # Calculate the total soaking time
    total_soak_time = grass_stains * GRASS_SOAK_TIME + marinara_stains * MARINARA_SOAK_TIME

    # Display the total soaking time
    result = total_soak_time
    return result

print(solution())