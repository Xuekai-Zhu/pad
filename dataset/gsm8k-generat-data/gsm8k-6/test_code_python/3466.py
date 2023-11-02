def solution():
    # Calculate UF's average score per game during the previous 24 games
    average_score = 720 / 24  

    # Calculate the total number of points their opponent scored in the championship game
    opponent_score = (average_score / 2 - 2) * 24 + 2  

    return opponent_score

print(solution())