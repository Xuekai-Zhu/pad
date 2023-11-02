def solution():
    """This weekend's football game matched the Seattle Seahawks with the Denver Broncos. The final score was 37-23, with the Seattle Seahawks taking the win. If a touchdown is worth 7 points and a field goal is worth 3 points, how many touchdowns did the Seattle Seahawks score if they scored 3 field goals during the game?"""
    # Define the points scored by the Seattle Seahawks and the number of field goals
    seahawks_points = 37
    field_goals = 3

    # Calculate the total points scored by the Seahawks from touchdowns
    touchdown_points = seahawks_points - (field_goals * 3)

    # Calculate the number of touchdowns scored by the Seahawks
    touchdowns = touchdown_points // 7

    # return the result
    result = touchdowns
    return result

print(solution())