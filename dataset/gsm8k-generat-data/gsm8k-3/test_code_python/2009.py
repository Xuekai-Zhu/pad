def solution():
    """The marching band has 110 members.  There are 4 times as many percussion players as there are woodwind, and twice as many woodwinds as brass.  How many brass players are there?"""
    # Define the number of members in the marching band
    total_members = 110

    # Calculate the number of brass players
    brass_players = total_members / (2 + 1 + 4*2)

    # Display the number of brass players
    result = brass_players
    return result

print(solution())