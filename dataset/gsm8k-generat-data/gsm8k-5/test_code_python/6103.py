def solution():
    initial_cans = 22  # Tim starts with 22 cans of soda
    cans_taken = 6  # Jeff takes 6 cans of soda from Tim
    cans_left = initial_cans - cans_taken  # Tim has cans_left cans of soda left

    # Tim buys half the amount of soda cans he had left
    bought_cans = cans_left / 2
    total_cans = cans_left + bought_cans  # Tim now has a total of total_cans cans of soda

    result = total_cans
    return result

print(solution())