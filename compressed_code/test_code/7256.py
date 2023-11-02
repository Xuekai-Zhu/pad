def solution():
    
    lawn_area = 22 * 36
    seed_coverage = 250
    bags_of_seed = 4
    total_coverage = seed_coverage * bags_of_seed
    leftover_coverage = total_coverage - lawn_area
    result = leftover_coverage
    return result

print(solution())