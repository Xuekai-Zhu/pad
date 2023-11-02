def solution():
    # Define the number of games given on Christmas and birthday
    christmas_games = 12
    birthday_games = 8

    # Calculate the total number of games Radhika had before Christmas and birthday
    initial_games = (christmas_games + birthday_games) * 2

    # Calculate the total number of games Radhika owns now
    total_games = initial_games + christmas_games + birthday_games
    result = total_games
    return result

print(solution())