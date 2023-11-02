def solution():
    total_games = 20
    win_points = 3
    draw_points = 1
    loss_points = 0

    # Calculate the number of points from wins
    win_total = 14 * win_points

    # Calculate the number of points from draws
    draw_total = (total_games - 14 - 2) * draw_points

    # Calculate the total number of points
    total_points = win_total + draw_total

    # Return the result
    result = total_points
    return result

print(solution())