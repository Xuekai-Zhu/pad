def solution():
    """Amanda is figuring out how many bags of grass seed she needs to buy to cover a new lot the city is turning into a park. The lot measures 120 feet by 60 feet. One section that measures 40 feet by 40 feet will be covered with concrete, and the rest needs to be covered in grass seeds. Each bag of grass seeds covers 56 square feet. How many bags of grass seeds does Amanda need?"""
    lot_area = 120 * 60
    concrete_area = 40 * 40
    grass_area = lot_area - concrete_area
    bags_needed = grass_area / 56
    result = bags_needed
    return result

print(solution())