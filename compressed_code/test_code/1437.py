def solution():
    
    lawn_area = 22 * 36
    bag_coverage = 250
    total_coverage = bag_coverage * 4
    used_coverage = min(lawn_area, total_coverage)
    leftover_coverage = total_coverage - used_coverage
    result = leftover_coverage
    return result

print(solution())