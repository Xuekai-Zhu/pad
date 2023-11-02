def solution():
    """While driving up a road, Philip passed through 5 intersections. 4 crosswalks marked each intersection with a total of 20 lines per crosswalk. Calculate the total number of lines of the crosswalks in the five intersections."""
    intersections = 5
    crosswalks = 4
    lines_per_crosswalk = 20
    total_lines = intersections * crosswalks * lines_per_crosswalk
    result = total_lines
    return result

print(solution())