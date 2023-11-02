def solution():
    """In a game, Samanta has 8 more points than Mark, and Mark has 50% more points than Eric. Eric has 6 points. How many points do Samanta, Mark, and Eric have in total?"""
    eric_points = 6
    mark_points = eric_points * 1.5
    samanta_points = mark_points + 8
    total_points = eric_points + mark_points + samanta_points
    result = total_points
    return result

print(solution())