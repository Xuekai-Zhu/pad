def solution():
    # Calculate the total number of points scored by Yolanda per game
    points_per_game = 345 / 15  

    # Calculate the total number of points scored per game from free throws and two-point baskets
    total_pts_FG_FT = 4 + (2*5)  

    # Calculate the number of points scored from three-point baskets per game
    pts_3PT = points_per_game - total_pts_FG_FT

    # Calculate the average number of three-point baskets per game
    avg_3PT = pts_3PT / 3

    result = avg_3PT
    return result

print(solution())