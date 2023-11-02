def solution():
    seeds_thrown_left = 20  # Mike throws 20 seeds to the birds on the left
    seeds_thrown_right = 2 * seeds_thrown_left  # Mike throws twice as much to the birds on the right
    seeds_thrown_additional = 30  # Mike throws 30 more seeds for the additional birds
    seeds_left = 30  # Mike has 30 seeds left to feed the last of the birds

    # Calculate the total number of seeds Mike threw
    total_seeds_thrown = seeds_thrown_left + seeds_thrown_right + seeds_thrown_additional + seeds_left

    result = total_seeds_thrown
    return result

print(solution())