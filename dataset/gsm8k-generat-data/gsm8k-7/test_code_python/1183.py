def solution():
    initial_count = 68
    gorilla_count = 6
    hippo_count = 1
    rhino_count = 3
    meerkat_count = 2

    # Calculate the total number of animals added/subtracted from the zoo
    total_change = -gorilla_count + hippo_count + rhino_count + (2 * meerkat_count)

    # Calculate the final animal count at the zoo
    final_count = initial_count + total_change

    # Calculate the number of lion cubs born
    lion_cub_count = final_count - 90
    result = lion_cub_count
    return result

print(solution())