def solution():
    """Jeff plays tennis for 2 hours. He scores a point every 5 minutes. He wins a match when he scores 8 points. How many games did he win?"""
    # Define the total playing time and the time it takes to score a point
    playing_time = 2 * 60  # 2 hours in minutes
    point_time = 5   # in minutes

    # Calculate the maximum number of points he could score during the playing time
    max_points = playing_time // point_time

    # Calculate the number of games won
    games_won = max_points // 8

    # Return the result
    result = games_won
    return result

print(solution())