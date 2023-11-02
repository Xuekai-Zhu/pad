def solution():
    """Bill needs to soak his clothes for 4 minutes to get rid of each grass stain and 7 additional minutes to get rid of each marinara stain. If his clothes have 3 grass stains and 1 marinara stain, how long does he need to soak them?"""
    # Define the time required to soak for one type of stain
    GRASS_STAIN_TIME = 4
    MARINARA_STAIN_TIME = 7

    # Define the number of grass and marinara stains
    grass_stains = 3
    marinara_stains = 1

    # Calculate the total time required to soak the clothes
    total_time = (grass_stains * GRASS_STAIN_TIME) + (marinara_stains * MARINARA_STAIN_TIME)

    # return the result
    result = total_time
    return result

print(solution())