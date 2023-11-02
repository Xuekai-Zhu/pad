def solution():
    """A baseball team has averaged 15 hits per game over their first 5 games. There are 11 players on the team. Their best player has 25 total hits. If the other players continue their average over the next 6 games, how many hits will each player average across the 6 games in total?"""
    # Define the total number of hits in the first 5 games and the number of players
    hits_first_5_games = 15 * 5
    num_players = 11

    # Subtract the hits of the best player from the total hits to get the hits of the other players
    hits_other_players = hits_first_5_games - 25

    # Calculate the average hits per player for the other players
    avg_hits_other_players = hits_other_players / (num_players - 1)

    # Calculate the total hits by the other players across the next 6 games
    total_hits_other_players = avg_hits_other_players * 6

    # Calculate the average hits per player across the next 6 games
    avg_hits_per_player = (total_hits_other_players + 25) / num_players

    # return the result
    result = avg_hits_per_player
    return result

print(solution())