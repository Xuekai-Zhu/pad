def solution():
    # Calculate the total number of points James scored in the season
    touchdowns = 4 * 15  # James scored 4 touchdowns per game and there are 15 games in the season
    conversions = 2 * 6  # James scored 2 point conversions 6 times during the season
    total_points = touchdowns * 6 + conversions

    # Calculate how many points James beat the old record by
    record = 300
    points_beaten = total_points - record
    result = points_beaten
    return result

print(solution())