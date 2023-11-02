def solution():
    """A father is buying sand to fill his son's new sandbox, but he is worried that the sand will be too heavy for his car.  The sandbox is square, with each side being 40 inches long.  If a 30-pound bag of sand is enough to fill 80 square inches of the sandbox to an adequate depth, how many pounds of sand are needed to fill the box completely?"""
    # Calculate the total area of the sandbox
    area = 40 * 40

    # Calculate the amount of sand needed to fill the sandbox to the right depth
    sand_needed = area / 80 * 30

    # Display the total weight of sand needed to fill the sandbox
    result = sand_needed
    return result

print(solution())