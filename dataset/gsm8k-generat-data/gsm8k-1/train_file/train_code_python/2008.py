def solution():
    """The marching band has 110 members. There are 4 times as many percussion players as there are woodwind, and twice as many woodwinds as brass. How many brass players are there?"""
    total_members = 110
    percussion_players = 4
    woodwind_players = percussion_players / 4
    brass_players = woodwind_players / 2
    total_non_brass_players = percussion_players + woodwind_players
    total_brass_players = total_members - total_non_brass_players
    result = total_brass_players
    return result

print(solution())