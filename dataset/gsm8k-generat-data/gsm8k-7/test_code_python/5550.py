def solution():
    num_intersections = 5
    num_crosswalks = 4
    lines_per_crosswalk = 20

    # Calculate the total number of lines in all crosswalks
    total_lines = num_intersections * num_crosswalks * lines_per_crosswalk
    result = total_lines
    return result

print(solution())