def solution():
    """A baseball team has averaged 15 hits per game over their first 5 games. There are 11 players on the team. Their best player has 25 total hits. If the other players continue their average over the next 6 games, how many hits will each player average across the 6 games in total?"""
    total_hits_first_5_games = 15 * 5
    hits_other_players_first_5_games = total_hits_first_5_games - 25
    num_other_players = 11 - 1
    avg_hits_other_players_first_5_games = hits_other_players_first_5_games / num_other_players
    total_hits_next_6_games = avg_hits_other_players_first_5_games * (num_other_players * 6)
    avg_hits_next_6_games = total_hits_next_6_games / (num_other_players * 6)
    result = avg_hits_next_6_games
    return result

print(solution())