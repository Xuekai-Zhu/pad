def solution():
    lot_area = 120 * 60  # The lot is 120 feet by 60 feet
    concrete_area = 40 * 40  # One section of 40 feet by 40 feet will be covered with concrete
    grass_area = lot_area - concrete_area  # The rest of the lot needs to be covered in grass
    bags_needed = grass_area / 56  # Each bag covers 56 square feet

    result = bags_needed
    return result

print(solution())