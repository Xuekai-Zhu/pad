def solution():
    """Clayton plays basketball on a team. He has played three games so far. In the first game, he scored 10 points. In the second game, he scored 14 points. In the third game, he scored 6 points. In the fourth game, he scored the average of his points from the first three games.  How many total points did Clayton score during the first four games?"""
    # Define the scores from the first three games
    game1_score = 10
    game2_score = 14
    game3_score = 6

    # Calculate the average score from the first three games
    avg_score = (game1_score + game2_score + game3_score) / 3

    # Calculate the score from the fourth game
    game4_score = avg_score

    # Calculate the total score from all four games
    total_score = game1_score + game2_score + game3_score + game4_score

    # Display the total score
    result = total_score
    return result

print(solution())