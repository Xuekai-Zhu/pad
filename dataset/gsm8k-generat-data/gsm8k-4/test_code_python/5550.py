def solution():
    """While driving up a road, Philip passed through 5 intersections. 4 crosswalks marked each intersection with a total of 20 lines per crosswalk. Calculate the total number of lines of the crosswalks in the five intersections."""
    # Define the number of intersections and crosswalks per intersection
    intersections = 5
    crosswalks_per_intersection = 4

    # Define the number of lines per crosswalk
    lines_per_crosswalk = 20

    # Calculate the total number of lines
    total_lines = intersections * crosswalks_per_intersection * lines_per_crosswalk

    # return the result
    result = total_lines
    return result

print(solution())