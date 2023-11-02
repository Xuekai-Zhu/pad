def solution():
    """In the Golden State Team, each player earned points. Draymond earned 12 points, Curry earned twice the points as Draymond, Kelly earned 9, Durant earned twice the points as Kelly, Klay earned half the points as Draymond. How many points did the Golden States have in total?"""
    # Calculate the points earned by each player
    draymond_points = 12
    curry_points = 2 * draymond_points
    kelly_points = 9
    durant_points = 2 * kelly_points
    klay_points = 0.5 * draymond_points

    # Calculate the total number of points earned by the team
    total_points = draymond_points + curry_points + kelly_points + durant_points + klay_points

    # return the result
    result = total_points
    return result

print(solution())