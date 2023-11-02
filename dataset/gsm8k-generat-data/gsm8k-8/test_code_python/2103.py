def solution():
    sandbox_area = 40 * 40  # area of sandbox in square inches
    sand_needed = sandbox_area * 80 / 80  # sand needed to fill sandbox to adequate depth
    total_sand_needed = sandbox_area * sand_needed / 80  # total sand needed to fill sandbox completely
    result = total_sand_needed
    return result

print(solution())