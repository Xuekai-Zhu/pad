def solution():
    games_bought = 200
    game_value_increase = 300
    total_value = games_bought + game_value_increase
    percent_sold = 40
    games_sold = total_value * (percent_sold / 100)
    result = games_sold
    return result

print(solution())