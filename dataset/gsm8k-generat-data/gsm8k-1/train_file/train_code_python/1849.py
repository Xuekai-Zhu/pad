def solution():
    """Drew is reseeding his lawn with grass seed. One bag of grass seed covers 250 square feet of lawn. His lawn is 22 feet from the house to the curb and 36 feet from side to side. He bought four bags of seed. How many extra square feet could the leftover grass seed cover after Drew reseeds his lawn?"""
    lawn_area = 22 * 36
    seed_coverage = 250
    bags_of_seed = 4
    total_coverage = seed_coverage * bags_of_seed
    leftover_coverage = total_coverage - lawn_area
    result = leftover_coverage
    return result

print(solution())