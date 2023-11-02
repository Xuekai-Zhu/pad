def solution():
    """A baseball team has averaged 15 hits per game over their first 5 games. There are 11 players on the team. Their best player has 25 total hits. If the other players continue their average over the next 6 games, how many hits will each player average across the 6 games in total?"""
    total_hits = 15 * 5 + 25
    other_players_hits = total_hits - 25
    average_hits_per_player = other_players_hits / (5 * 10)
    total_hits_next_6_games = average_hits_per_player * 11 * 6
    average_hits_next_6_games_per_player = total_hits_next_6_games / (6 * 11)
    result = average_hits_next_6_games_per_player
    return result

print(solution())