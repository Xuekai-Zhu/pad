def solution():
    """This weekend's football game matched the Seattle Seahawks with the Denver Broncos. The final score was 37-23, with the Seattle Seahawks taking the win. If a touchdown is worth 7 points and a field goal is worth 3 points, how many touchdowns did the Seattle Seahawks score if they scored 3 field goals during the game?"""
    # Define the values of a touchdown and a field goal
    TOUCHDOWN_POINTS = 7
    FIELD_GOAL_POINTS = 3

    # Define the total number of points scored by the Seattle Seahawks
    total_score = 37

    # Define the number of field goals scored by the Seattle Seahawks
    field_goals = 3

    # Calculate the total number of points scored by the Seattle Seahawks from touchdowns alone
    touchdowns_only_points = total_score - field_goals*FIELD_GOAL_POINTS

    # Calculate the number of touchdowns scored by the Seattle Seahawks
    touchdowns = touchdowns_only_points // TOUCHDOWN_POINTS

    # Display the number of touchdowns scored by the Seattle Seahawks
    result = touchdowns
    return result

print(solution())