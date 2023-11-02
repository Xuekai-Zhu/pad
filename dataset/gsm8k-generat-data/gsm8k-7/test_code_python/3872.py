def solution():
    home_game_points = 62
    
    # Calculate the points scored at the first away game
    away_game1_points = home_game_points / 2
    
    # Calculate the points scored at the second away game
    away_game2_points = away_game1_points + 18
    
    # Calculate the points scored at the third away game
    away_game3_points = away_game2_points + 2
    
    # Calculate the total points scored in all games except the last home game
    total_points = away_game1_points + away_game2_points + away_game3_points
    
    # Calculate the total points needed to reach four times the points of the last home game
    total_points_needed = home_game_points * 4 - home_game_points
    
    # Calculate the points needed in the next game to reach the target total
    next_game_points = total_points_needed - total_points
    
    result = next_game_points
    return result

print(solution())