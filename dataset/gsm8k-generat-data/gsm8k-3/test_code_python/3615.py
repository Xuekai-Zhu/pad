def solution():
    """A baseball team has averaged 15 hits per game over their first 5 games. There are 11 players on the team. Their best player has 25 total hits. If the other players continue their average over the next 6 games, how many hits will each player average across the 6 games in total?"""
    # Define the number of games played and the number of players on the team
    GAMES_PLAYED = 5
    NUM_PLAYERS = 11

    # Define the total hits for the team over the first 5 games and the number of hits for the best player
    TOTAL_HITS = 15 * GAMES_PLAYED
    BEST_PLAYER_HITS = 25

    # Calculate the total hits for the other 10 players over the first 5 games
    OTHER_PLAYERS_HITS = TOTAL_HITS - BEST_PLAYER_HITS

    # Calculate the average hits per player for the other players over the first 5 games
    AVG_OTHER_PLAYERS_HITS = OTHER_PLAYERS_HITS / (NUM_PLAYERS - 1)

    # Calculate the total hits for the other players across the next 6 games
    TOTAL_OTHER_PLAYERS_HITS = AVG_OTHER_PLAYERS_HITS * NUM_PLAYERS * 6

    # Calculate the average hits per player for the other players across the next 6 games
    AVG_OTHER_PLAYERS_HITS_6_GAMES = TOTAL_OTHER_PLAYERS_HITS / (NUM_PLAYERS - 1) / 6

    # Display the average hits per player for the other players across the next 6 games
    result = AVG_OTHER_PLAYERS_HITS_6_GAMES
    return result

print(solution())