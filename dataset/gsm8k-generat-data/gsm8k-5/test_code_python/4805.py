def solution():
    total_players = 40  # Total number of chess players on the island
    never_lost_players = total_players / 4  # A quarter of the players have never lost to an AI
    lost_players = total_players - never_lost_players  # The remaining players must have lost at least once
    result = lost_players
    return result

print(solution())