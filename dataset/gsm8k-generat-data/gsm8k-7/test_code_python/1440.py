def solution():
    total_games = 20
    wins = 14
    losses = 2
    draws = total_games - wins - losses

    # Calculate the total number of points earned from wins
    win_points = wins * 3

    # Calculate the total number of points earned from draws
    draw_points = draws * 1

    # Calculate the total number of points earned in the season
    total_points = win_points + draw_points

    result = total_points
    return result

print(solution())