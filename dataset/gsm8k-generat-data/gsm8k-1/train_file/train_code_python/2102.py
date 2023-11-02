def solution():
    """A father is buying sand to fill his son's new sandbox, but he is worried that the sand will be too heavy for his car. The sandbox is square, with each side being 40 inches long. If a 30-pound bag of sand is enough to fill 80 square inches of the sandbox to an adequate depth, how many pounds of sand are needed to fill the box completely?"""
    sandbox_area = 40 * 40
    sand_needed = sandbox_area * 80 / (1 * 1)
    pounds_needed = sand_needed / 30
    result = pounds_needed
    return result

print(solution())