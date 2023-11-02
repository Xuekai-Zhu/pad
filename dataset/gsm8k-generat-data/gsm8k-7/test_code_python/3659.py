def solution():
    # Initialize variables
    x = 12  # number of games given on Christmas
    y = 8  # number of games given on birthday
    old_games = (x + y) / 2  # number of games Radhika already owned
    total_games = x + y + old_games  # total number of games Radhika owns now

    result = total_games
    return result

print(solution())