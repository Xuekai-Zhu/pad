def solution():
    """On Wednesday, 37 students played kickball. On Thursday, 9 fewer students played kickball. How many students played kickball on Wednesday and Thursday?"""
    wednesday_players = 37
    thursday_players = wednesday_players - 9
    total_players = wednesday_players + thursday_players
    result = total_players
    return result

print(solution())