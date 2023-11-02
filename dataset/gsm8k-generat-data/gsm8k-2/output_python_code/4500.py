def solution():
    """Roosevelt High school plays a basketball tournament with Greendale High school. Roosevelt high school scores 30 points in the first game, half as much in the second game, and triple as much as the second game in the third game. At the end of the tournament, Roosevelt high school receives 50 bonus points and Greendale high school has 10 points less than Roosevelt high school. How many points does Greendale high school have?"""
    roosevelt_first_game = 30
    roosevelt_second_game = roosevelt_first_game / 2
    roosevelt_third_game = roosevelt_second_game * 3
    roosevelt_total_score = roosevelt_first_game + roosevelt_second_game + roosevelt_third_game + 50
    greendale_total_score = roosevelt_total_score - 10
    result = greendale_total_score
    return result

print(solution())