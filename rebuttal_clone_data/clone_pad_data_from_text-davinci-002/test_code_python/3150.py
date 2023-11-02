def solution():
    money_needed = 500
    money_received = 200 + 150
    money_per_game = 7.5
    games_needed = (money_needed - money_received) / money_per_game
    result = games_needed
    return result

print(solution())