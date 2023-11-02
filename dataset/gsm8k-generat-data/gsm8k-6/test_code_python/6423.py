def solution():
    # Calculate the current win percentage of the team
    current_wins = 35
    current_total = 50 + 25  # total number of games left to play plus the games already played
    current_percentage = (current_wins / current_total) * 100

    # Calculate the number of games the team must win to achieve a 64% win percentage for the entire season
    target_percentage = 64
    target_wins = (current_total * target_percentage / 100) - current_wins
    result = round(target_wins)  # round up to the nearest integer
    return result

print(solution())