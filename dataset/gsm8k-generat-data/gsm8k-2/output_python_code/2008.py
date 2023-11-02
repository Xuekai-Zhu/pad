def solution():
    """The marching band has 110 members. There are 4 times as many percussion players as there are woodwind, and twice as many woodwinds as brass. How many brass players are there?"""
    total_members = 110
    percussion_players = 4 * x
    woodwind_players = 2 * x
    brass_players = total_members / (1 + 4 + 2)
    result = brass_players
    return result

print(solution())