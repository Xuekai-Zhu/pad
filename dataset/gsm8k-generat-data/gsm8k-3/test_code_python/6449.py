def solution():
    """Carter plays soccer on the school team.  On average, he scores 4 goals per game.  Shelby scores half as many as Carter per game on average.  And Judah, on average, scores three less than twice as many goals per game as Shelby.  If these three teammates are the only ones that score goals for the school team, what is the average total number of goals scored by the team per game?"""
    # Define the average number of goals per game for each player
    CARTER_GOALS = 4
    SHELBY_GOALS = CARTER_GOALS / 2
    JUDAH_GOALS = (2 * SHELBY_GOALS) - 3

    # Calculate the average total number of goals scored by the team per game
    avg_goals = CARTER_GOALS + SHELBY_GOALS + JUDAH_GOALS

    # Display the average total number of goals scored by the team per game
    result = avg_goals
    return result

print(solution())