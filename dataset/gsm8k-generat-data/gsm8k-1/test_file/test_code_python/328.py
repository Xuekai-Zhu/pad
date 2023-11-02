def solution():
    """There are 220 castles in Scotland. 40 percent of them are ruins, and half of the ruined castles are unmanned. How many unmanned ruined castles are there in Scotland?"""
    total_castles = 220
    ruined_castles = total_castles * 0.4
    unmanned_ruined_castles = ruined_castles * 0.5
    result = unmanned_ruined_castles
    return result

print(solution())