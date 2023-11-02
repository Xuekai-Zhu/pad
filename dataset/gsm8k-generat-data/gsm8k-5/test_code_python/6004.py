def solution():
    large_glass_capacity = 50  # It takes 50 large jelly beans to fill up a large drinking glass
    small_glass_capacity = large_glass_capacity / 2  # It takes half that amount to fill up a small drinking glass
    num_large_glasses = 5  # There are 5 large drinking glasses
    num_small_glasses = 3  # There are 3 small drinking glasses

    # Calculate the total number of jelly beans needed to fill up all glasses
    total_jelly_beans = (large_glass_capacity * num_large_glasses) + (small_glass_capacity * num_small_glasses)
    result = total_jelly_beans
    return result

print(solution())