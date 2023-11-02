def solution():
    """During a soccer game, in the first half, Team A scored 8 points, and Team B scored only half as many points. In the second half, Team B was able to get as many points as Team A in the first half, and Team A scored only 2 goals less than Team B. How many goals did both teams score during the whole match?"""

    # Calculate the number of points scored by Team B in the first half
    teamB_first_half = 8 / 2

    # Calculate the number of points scored by Team A in the second half
    teamA_second_half = teamB_first_half

    # Calculate the number of points scored by Team B in the second half
    teamB_second_half = 8 - 2

    # Calculate the total number of points for both teams
    total_points = 8 + teamB_first_half + teamA_second_half + teamB_second_half

    # return the result
    result = total_points
    return result

print(solution())