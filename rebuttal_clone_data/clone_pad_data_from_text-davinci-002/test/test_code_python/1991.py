def solution():
    lot_length = 120
    lot_width = 60
    concrete_area = 40 * 40
    grass_area = (lot_length * lot_width) - concrete_area
    area_to_cover =grass_area 
    seed_coverage = 56
    number_of_bags = area_to_cover / seed_coverage
    result = number_of_bags
    return result

print(solution())