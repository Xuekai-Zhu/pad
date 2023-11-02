def solution():
    """In a basketball game, Tobee scored 4 points. Jay scored 6 more than Tobee and Sean scored 2 less than the points of Tobee and Jay together. If Tobee, Jay, and Sean are on the same team, how many points did they score for their team?"""
    # Define the points scored by Tobee
    tobee_points = 4

    # Calculate the points scored by Jay
    jay_points = tobee_points + 6

    # Calculate the total points scored by Tobee and Jay
    total_points = tobee_points + jay_points

    # Calculate the points scored by Sean
    sean_points = total_points - 2

    # Calculate the total points scored by the team
    team_points = tobee_points + jay_points + sean_points

    # Return the result
    result = team_points
    return result

print(solution())