def solution():
    """The Tampa Bay Bucs have 13 football players and 16 cheerleaders. If 10 football players and 4 cheerleaders quit, how many football players and cheerleaders are left?"""
    # Define the initial number of football players and cheerleaders
    football_players = 13
    cheerleaders = 16

    # Subtract the number of players who quit
    football_players -= 10
    cheerleaders -= 4

    # return the result
    result = (football_players, cheerleaders)
    return result

print(solution())