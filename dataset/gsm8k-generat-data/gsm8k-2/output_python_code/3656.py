def solution():
    """The Tampa Bay Bucs have 13 football players and 16 cheerleaders. If 10 football players and 4 cheerleaders quit, how many football players and cheerleaders are left?"""
    initial_football_players = 13
    initial_cheerleaders = 16
    quitting_football_players = 10
    quitting_cheerleaders = 4
    remaining_football_players = initial_football_players - quitting_football_players
    remaining_cheerleaders = initial_cheerleaders - quitting_cheerleaders
    result = (remaining_football_players, remaining_cheerleaders)
    return result

print(solution())