def solution():
    sandbox_length = 40
    sandbox_width = 40
    sandbox_area = sandbox_length * sandbox_width
    sand_area_coverage = 80
    sand_pounds = 30
    total_sand_pounds = sandbox_area / sand_area_coverage * sand_pounds
    result = total_sand_pounds
    return result

print(solution())