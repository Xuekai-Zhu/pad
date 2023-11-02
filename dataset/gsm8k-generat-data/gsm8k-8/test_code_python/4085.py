def solution():
    # Define the number of ants in the first anthill
    ants_in_first_anthill = 100

    # Define the reduction factor for each anthill
    reduction_factor = 0.2

    # Calculate the number of ants in the second anthill
    ants_in_second_anthill = ants_in_first_anthill * (1 - reduction_factor)

    # Calculate the number of ants in the third anthill
    ants_in_third_anthill = ants_in_second_anthill * (1 - reduction_factor)

    result = ants_in_third_anthill
    return result

print(solution())