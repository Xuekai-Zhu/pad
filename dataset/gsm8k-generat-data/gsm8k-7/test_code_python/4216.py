def solution():
    draymond_points = 12
    curry_points = 2 * draymond_points
    kelly_points = 9
    durant_points = 2 * kelly_points
    klay_points = 0.5 * draymond_points

    # Calculate the total points earned by the team
    total_points = draymond_points + curry_points + kelly_points + durant_points + klay_points
    result = total_points
    return result

print(solution())