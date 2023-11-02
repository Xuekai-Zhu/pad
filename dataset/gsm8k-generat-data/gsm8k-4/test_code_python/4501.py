def solution():
    """Roosevelt High school plays a basketball tournament with Greendale High school. Roosevelt high school scores 30 points in the first game, half as much in the second game, and triple as much as the second game in the third game. At the end of the tournament, Roosevelt high school receives 50 bonus points and Greendale high school has 10 points less than Roosevelt high school. How many points does Greendale high school have?"""
    # Calculate the total points Roosevelt High school scored in the tournament
    first_game_points = 30
    second_game_points = first_game_points / 2
    third_game_points = second_game_points * 3

    roosevelt_total_points = first_game_points + second_game_points + third_game_points + 50

    # Calculate the points for Greendale High school
    greendale_points = roosevelt_total_points - 10

    # Return the result
    result = greendale_points
    return result

print(solution())