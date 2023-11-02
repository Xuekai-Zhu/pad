def solution():
    """On the island of Castor, there are 40 chess players. A quarter of the island's chess players have never lost to an AI. How many people on the island have lost to a computer, at least once?"""
    # Define the total number of chess players
    total_chess_players = 40

    # Calculate the number of chess players who have never lost to an AI
    never_lost_players = total_chess_players / 4

    # Calculate the number of chess players who have lost to an AI, at least once
    lost_players = total_chess_players - never_lost_players

    # Return the result
    result = lost_players
    return result

print(solution())