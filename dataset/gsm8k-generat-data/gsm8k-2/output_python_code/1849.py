def solution():
    """Drew is reseeding his lawn with grass seed. One bag of grass seed covers 250 square feet of lawn. His lawn is 22 feet from the house to the curb and 36 feet from side to side. He bought four bags of seed. How many extra square feet could the leftover grass seed cover after Drew reseeds his lawn?"""
    lawn_area = 22 * 36
    bag_coverage = 250
    total_coverage = bag_coverage * 4
    used_coverage = min(lawn_area, total_coverage)
    leftover_coverage = total_coverage - used_coverage
    result = leftover_coverage
    return result

print(solution())