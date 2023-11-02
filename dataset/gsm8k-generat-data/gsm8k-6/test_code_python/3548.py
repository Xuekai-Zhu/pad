def solution():
    # Calculate the total area of the lot
    total_area = 120 * 60  # the lot measures 120 feet by 60 feet
    # Calculate the area of the section covered by concrete
    concrete_area = 40 * 40  # the section that measures 40 feet by 40 feet will be covered with concrete
    # Calculate the area that needs to be covered in grass seeds
    grass_area = total_area - concrete_area
    # Calculate the number of bags of grass seeds Amanda needs to buy
    bags_of_grass_seeds = grass_area/56  # each bag of grass seeds covers 56 square feet
    result = bags_of_grass_seeds
    return result

print(solution())