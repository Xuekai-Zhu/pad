def solution():
    # Find the total number of games Radhika was given
    total_given = 12 + 8  

    # Find the number of games Radhika had before Christmas and her birthday
    had_before = total_given / 2  

    # Find the total number of games she owns now
    total_games = had_before + total_given  

    result = total_games
    return result

print(solution())