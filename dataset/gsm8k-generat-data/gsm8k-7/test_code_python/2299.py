def solution():
    archibald_games = 12
    brother_games = 18

    # Calculate the total number of games played
    total_games = archibald_games + brother_games

    # Calculate the percentage of games won by Archibald
    archibald_percentage = archibald_games / total_games * 100

    result = archibald_percentage
    return result

print(solution())