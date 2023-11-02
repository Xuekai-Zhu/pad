def solution():
    """Lola plays basketball on her school team. Her team scored twice at many points at their last home game than their first away game. At the second away game, they scored eighteen points more than the previous away game. At the third away game, they scored two more points than at their second. If Lola’s team scored 62 points at their last home game, how many points do they have to score in their next game to bring their cumulative points up to four times the score from their last home game?"""
    first_away_game = 0 # unknown variable
    second_away_game = first_away_game + 18 + 2
    third_away_game = second_away_game + 2
    home_game = 62
    total_points = home_game + first_away_game + second_away_game + third_away_game
    points_needed = 4 * home_game - total_points
    result = points_needed
    return result

print(solution())