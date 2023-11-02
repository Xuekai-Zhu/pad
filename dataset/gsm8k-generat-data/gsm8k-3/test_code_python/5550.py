def solution():
    """While driving up a road, Philip passed through 5 intersections. 4 crosswalks marked each intersection with a total of 20 lines per crosswalk. Calculate the total number of lines of the crosswalks in the five intersections."""
    # Define the number of crosswalks per intersection and the number of lines per crosswalk
    CROSSWALKS_PER_INTERSECTION = 4
    LINES_PER_CROSSWALK = 20

    # Define the number of intersections passed through
    intersections = 5

    # Calculate the total number of lines in the crosswalks
    total_lines = intersections * CROSSWALKS_PER_INTERSECTION * LINES_PER_CROSSWALK

    result = total_lines
    return result

print(solution())