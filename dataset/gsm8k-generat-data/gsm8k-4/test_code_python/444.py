def solution():
    """Reggie and his brother are having a basketball shooting contest. They each get to take 10 shots. Layups are worth 1 point, free throws are worth 2 points, and anything further away is worth 3 points. Reggie makes 3 layups, two free throws, and one long shot. His brother only shoots long shots and makes 4 of them. How many points does Reggie lose by?"""
    # Define the point values for each type of shot
    LAYUP_POINTS = 1
    FREE_THROW_POINTS = 2
    LONG_SHOT_POINTS = 3

    # Define the number of shots each player gets
    NUM_SHOTS = 10

    # Reggie's points
    reggie_points = (3 * LAYUP_POINTS) + (2 * FREE_THROW_POINTS) + (1 * LONG_SHOT_POINTS)

    # Calculate his brother's points
    brother_points = 4 * LONG_SHOT_POINTS

    # Calculate the point differential
    point_differential = brother_points - reggie_points

    # return the result
    result = point_differential
    return result

print(solution())