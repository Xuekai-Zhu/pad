def solution():
    lot_area = 120 * 60
    section_area = 40 * 40
    grass_area = lot_area - section_area
    bag_coverage = 56
    num_bags = grass_area / bag_coverage
    result = num_bags
    return result

print(solution())