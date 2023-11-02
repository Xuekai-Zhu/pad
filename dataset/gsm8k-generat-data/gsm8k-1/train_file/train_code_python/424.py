def solution():
    """Calvin and Paislee played a pool game where points were awarded for winning a round. If Calvin had scored 500 points and Paislee 3/4 times as many points as Calvin, how many points was Paislee required to achieve to have a chance of tying the game?"""
    calvin_points = 500
    paislee_points = 3/4 * calvin_points
    points_needed = (calvin_points - paislee_points) + calvin_points
    result = points_needed
    return result

print(solution())