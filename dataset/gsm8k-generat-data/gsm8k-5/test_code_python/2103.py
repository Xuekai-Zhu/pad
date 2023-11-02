def solution():
    sandbox_area = 40 * 40  # The sandbox is square, with each side being 40 inches long
    sand_needed_per_area = 30 / 80  # A 30-pound bag of sand is enough to fill 80 square inches of the sandbox to an adequate depth
    total_sand_needed = sand_needed_per_area * sandbox_area  # Calculate the total amount of sand needed to fill the sandbox completely
    result = total_sand_needed
    return result

print(solution())