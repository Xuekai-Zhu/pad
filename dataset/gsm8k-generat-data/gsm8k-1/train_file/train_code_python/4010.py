def solution():
    """Hannah hangs a 2 foot by 4 foot painting on a 5 foot by 10 foot wall. What percentage of the wall is taken up by the painting?"""
    painting_area = 2 * 4
    wall_area = 5 * 10
    percentage_taken_up = (painting_area / wall_area) * 100
    result = percentage_taken_up
    return result

print(solution())