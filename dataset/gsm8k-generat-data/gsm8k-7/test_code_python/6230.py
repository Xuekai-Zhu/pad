def solution():
    num_apples = 2
    num_slices_per_apple = 8
    fraction_given = 3/8
    fraction_eaten = 1/2
    
    # Calculate the total number of slices
    total_slices = num_apples * num_slices_per_apple

    # Calculate the number of slices given to Jerry
    given_slices = total_slices * fraction_given

    # Calculate the number of remaining slices after giving some to Jerry
    remaining_slices = total_slices - given_slices

    # Calculate the number of slices eaten by Tom
    eaten_slices = remaining_slices * fraction_eaten

    # Calculate the final number of slices Tom has
    final_slices = remaining_slices - eaten_slices
    result = final_slices
    return result

print(solution())