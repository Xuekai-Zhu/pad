def solution():
    """Reggie and his brother are having a basketball shooting contest. They each get to take 10 shots. Layups are worth 1 point, free throws are worth 2 points, and anything further away is worth 3 points. Reggie makes 3 layups, two free throws, and one long shot. His brother only shoots long shots and makes 4 of them. How many points does Reggie lose by?"""
    reggie_points = (3*1) + (2*2) + (1*3)
    brother_points = 4*3
    point_difference = brother_points - reggie_points
    result = point_difference
    return result

print(solution())