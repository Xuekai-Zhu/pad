def solution():
    lines_per_crosswalk = 20  # There are 20 lines per crosswalk
    crosswalks_per_intersection = 4  # There are 4 crosswalks per intersection
    intersections_passed = 5  # Philip passed through 5 intersections

    # Calculate the total number of lines in the crosswalks
    total_lines = lines_per_crosswalk * crosswalks_per_intersection * intersections_passed
    result = total_lines
    return result

print(solution())