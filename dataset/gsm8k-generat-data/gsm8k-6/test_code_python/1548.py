def solution():
    # Calculate how many bugs are left in the garden after one spraying and introducing spiders
    bugs_after_spraying = 0.8 * 400  # reduces total bug population to 80% of what it was previously
    bugs_after_spiders = bugs_after_spraying - (12 * 7)  # each spider he introduces eats 7 bugs
    result = bugs_after_spiders
    return result

print(solution())