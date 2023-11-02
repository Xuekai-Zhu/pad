def solution():
    """During a soccer game, in the first half, Team A scored 8 points, and Team B scored only half as many points.
    In the second half, Team B was able to get as many points as Team A in the first half, and Team A scored only 2 goals less than Team B.
    How many goals did both teams score during the whole match?"""
    
    teamA_first_half = 8
    teamB_first_half = teamA_first_half / 2
    teamA_second_half = teamB_first_half
    teamB_second_half = teamA_first_half - 2
    
    total_goals = teamA_first_half + teamB_first_half + teamA_second_half + teamB_second_half
    result = total_goals
    return result

print(solution())