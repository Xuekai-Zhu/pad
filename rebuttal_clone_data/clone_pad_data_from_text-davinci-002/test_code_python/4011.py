def solution():
    painting_width = 2
    painting_height = 4
    wall_width = 5
    wall_height = 10
    painting_area = painting_width * painting_height
    wall_area = wall_width * wall_height
    percent_coverage = painting_area / wall_area * 100
    result = percent_coverage
    return result

print(solution())