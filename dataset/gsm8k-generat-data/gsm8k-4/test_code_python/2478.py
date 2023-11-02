def solution():
    """In a game, Samanta has 8 more points than Mark, and Mark has 50% more points than Eric. Eric has 6 points. How many points do Samanta, Mark, and Eric have in total?"""
    # Define Eric's points
    eric_points = 6

    # Calculate Mark's points (50% more than Eric's points)
    mark_points = eric_points * 1.5

    # Calculate Samanta's points (8 more than Mark's points)
    samanta_points = mark_points + 8

    # Calculate the total points
    total_points = eric_points + mark_points + samanta_points

    # return the result
    result = total_points
    return result

print(solution())