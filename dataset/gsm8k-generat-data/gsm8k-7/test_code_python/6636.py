def solution():
    # Calculate the total number of seeds produced by the original plant
    num_seeds_orig = 50

    # Calculate the number of seeds that germinated from the original plant
    num_seeds_germ = num_seeds_orig / 2

    # Calculate the total number of seeds produced by the new plants
    num_seeds_new = num_seeds_germ * num_seeds_orig

    # Calculate the total number of seeds produced in two months' time
    total_seeds = num_seeds_orig + num_seeds_new
    result = total_seeds
    return result

print(solution())