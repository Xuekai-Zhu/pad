def solution():
    
    slices_per_pizza = 12
    total_slices = slices_per_pizza * 6
    games_played = 8
    goals_per_game = total_slices / games_played
    result = goals_per_game
    return result

print(solution())