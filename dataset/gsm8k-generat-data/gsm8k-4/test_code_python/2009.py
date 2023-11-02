def solution():
    """The marching band has 110 members. There are 4 times as many percussion players as there are woodwind, and twice as many woodwinds as brass. How many brass players are there?"""
    # Define the total number of members and the number of brass players
    total_members = 110
    brass_players = None

    # Calculate the number of woodwind players
    woodwind_players = total_members / (4 + 2 + 1)

    # Calculate the number of percussion players
    percussion_players = 4 * woodwind_players

    # Calculate the number of brass players
    brass_players = total_members - (woodwind_players + percussion_players)

    # return the result
    result = brass_players
    return result

print(solution())