def solution():
    """It takes 50 large jelly beans to fill up a large drinking glass. It takes half that amount to fill up a small drinking glass. If there are 5 large drinking glasses and 3 small ones, how many jellybeans will it take to fill them up?"""
    large_glass_capacity = 50
    small_glass_capacity = large_glass_capacity / 2
    num_large_glasses = 5
    num_small_glasses = 3
    total_jelly_beans = (large_glass_capacity * num_large_glasses) + (small_glass_capacity * num_small_glasses)
    result = total_jelly_beans
    return result

print(solution())