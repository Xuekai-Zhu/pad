def solution():
    """Lola plays basketball on her school team. Her team scored twice at many points at their last home game than their first away game. At the second away game, they scored eighteen points more than the previous away game. At the third away game, they scored two more points than at their second. If Lola’s team scored 62 points at their last home game, how many points do they have to score in their next game to bring their cumulative points up to four times the score from their last home game?"""
    # Define the number of points scored at the last home game
    home_game_points = 62

    # Calculate the number of points scored at the first away game
    away_game1_points = home_game_points / 2

    # Calculate the number of points scored at the second away game
    away_game2_points = away_game1_points + 18

    # Calculate the number of points scored at the third away game
    away_game3_points = away_game2_points + 2

    # Calculate the total number of points scored at all away games
    away_game_total_points = away_game1_points + away_game2_points + away_game3_points

    # Calculate the number of points needed in the next game to reach four times the score of the last home game
    points_needed = (4 * home_game_points) - away_game_total_points

    # Display the number of points needed
    result = points_needed
    return result

print(solution())