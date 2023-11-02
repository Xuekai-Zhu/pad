def solution():
    """A soccer team has 24 players. They have scored 150 goals on the season. There have been 15 games played. 1/3 of the players have averaged 1 goal each per game. How many total goals have the other players scored?"""
    total_players = 24
    total_goals = 150
    total_games = 15
    good_players = total_players // 3
    good_player_goals = good_players * total_games
    good_player_avg = good_player_goals / good_players
    other_players = total_players - good_players
    other_player_goals = total_goals - good_player_goals
    other_player_avg = other_player_goals / (other_players * total_games)
    other_player_total_goals = other_players * total_games * other_player_avg

    result = other_player_total_goals
    return result

print(solution())