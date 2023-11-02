def solution():
    """Roosevelt High school plays a basketball tournament with Greendale High school. Roosevelt high school scores 30 points in the first game, half as much in the second game, and triple as much as the second game in the third game. At the end of the tournament, Roosevelt high school receives 50 bonus points and Greendale high school has 10 points less than Roosevelt high school. How many points does Greendale high school have?"""
    roosevelt_first = 30
    roosevelt_second = roosevelt_first / 2
    roosevelt_third = roosevelt_second * 3
    roosevelt_total = roosevelt_first + roosevelt_second + roosevelt_third + 50
    greendale_total = roosevelt_total - 10
    result = greendale_total
    return result

print(solution())