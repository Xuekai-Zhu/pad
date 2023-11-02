def solution():
    """In the Golden State Team, each player earned points. Draymond earned 12 points, Curry earned twice the points as Draymond, Kelly earned 9, Durant earned twice the points as Kelly, Klay earned half the points as Draymond. How many points did the Golden States have in total?"""
    draymond_points = 12
    curry_points = draymond_points * 2
    kelly_points = 9
    durant_points = kelly_points * 2
    klay_points = draymond_points / 2
    total_points = draymond_points + curry_points + kelly_points + durant_points + klay_points
    result = total_points
    return result

print(solution())