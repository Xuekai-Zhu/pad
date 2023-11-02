def solution():
    # Define the starting number of animals and the number of animals gained/lost
    starting_num = 68
    gorilla_loss = 6
    hippo_gain = 1
    rhino_gain = 3
    lioness_cub_gain = 0
    meerkat_gain = 0

    # Calculate the final number of animals
    final_num = starting_num - gorilla_loss + hippo_gain + rhino_gain + lioness_cub_gain + meerkat_gain

    # Set up equation to solve for the number of lion cubs
    # x + 2x = total_num - starting_num (where x is the number of lion cubs)
    total_num = 90
    lion_cub_num = (total_num - starting_num) / 3

    result = lion_cub_num
    return result

print(solution())