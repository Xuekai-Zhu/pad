def solution():
    calvin_points = 500  # Calvin scored 500 points
    paislee_points = (3/4) * calvin_points  # Paislee scored 3/4 times as many points as Calvin
    required_points = calvin_points - paislee_points + 1  # To tie the game, Paislee needs one more point than Calvin

    result = required_points
    return result

print(solution())