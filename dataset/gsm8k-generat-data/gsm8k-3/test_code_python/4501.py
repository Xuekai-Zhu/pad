def solution():
    """Roosevelt High school plays a basketball tournament with Greendale High school. Roosevelt high school scores 30 points in the first game, half as much in the second game, and triple as much as the second game in the third game. At the end of the tournament, Roosevelt high school receives 50 bonus points and Greendale high school has 10 points less than Roosevelt high school. How many points does Greendale high school have?"""
    # Calculate Roosevelt High School's score for each game
    game1 = 30
    game2 = game1 / 2
    game3 = game2 * 3

    # Calculate Roosevelt High School's total score
    total_score = game1 + game2 + game3 + 50

    # Calculate Greendale High School's score
    greendale_score = total_score - 10

    # Display Greendale High School's score
    result = greendale_score
    return result

print(solution())