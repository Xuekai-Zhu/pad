def solution():
    """Hannah hangs a 2 foot by 4 foot painting on a 5 foot by 10 foot wall. What percentage of the wall is taken up by the painting?"""
    painting_area = 2 * 4  # in square feet
    wall_area = 5 * 10  # in square feet
    percent_of_wall_taken_up = (painting_area / wall_area) * 100
    result = percent_of_wall_taken_up
    return result

print(solution())