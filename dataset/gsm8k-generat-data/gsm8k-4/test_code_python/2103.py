def solution():
    """A father is buying sand to fill his son's new sandbox, but he is worried that the sand will be too heavy for his car.
    The sandbox is square, with each side being 40 inches long. If a 30-pound bag of sand is enough to fill 80 square inches of
    the sandbox to an adequate depth, how many pounds of sand are needed to fill the box completely?"""
    # Define the length of one side of the sandbox in inches
    side_length = 40

    # Calculate the total area of the sandbox in square inches
    total_area = side_length ** 2

    # Calculate the number of bags needed to fill 1 square inch to the desired depth
    bags_per_square_inch = 1 / 80 / 30

    # Calculate the total number of bags needed to fill the entire sandbox to the desired depth
    total_bags = total_area * bags_per_square_inch

    # Calculate the weight of sand needed to fill the sandbox completely
    sand_weight = total_bags * 30

    result = sand_weight
    return result

print(solution())