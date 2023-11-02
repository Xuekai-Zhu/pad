def solution():
    """Reggie and his brother are having a basketball shooting contest. They each get to take 10 shots. Layups are worth 1 point, free throws are worth 2 points, and anything further away is worth 3 points. Reggie makes 3 layups, two free throws, and one long shot. His brother only shoots long shots and makes 4 of them. How many points does Reggie lose by?"""
    # Define the point value of each type of shot
    LAYUP_VALUE = 1
    FREE_THROW_VALUE = 2
    LONG_SHOT_VALUE = 3

    # Define the number of shots each player takes
    REGGIE_SHOTS = 10
    BROTHER_SHOTS = 10

    # Define the number of each type of shot each player makes
    reggie_layups = 3
    reggie_free_throws = 2
    reggie_long_shots = 1
    brother_long_shots = 4

    # Calculate Reggie's total score
    reggie_score = (reggie_layups * LAYUP_VALUE) + (reggie_free_throws * FREE_THROW_VALUE) + (reggie_long_shots * LONG_SHOT_VALUE)

    # Calculate Reggie's brother's total score
    brother_score = brother_long_shots * LONG_SHOT_VALUE

    # Find the difference between the scores
    point_difference = brother_score - reggie_score

    # Return the point difference
    result = point_difference
    return result

print(solution())