def solution():
    
    total_points = 345
    total_games = 15
    free_throws_per_game = 4
    two_pointers_per_game = 5
    three_pointers_per_game = (total_points - (free_throws_per_game * total_games) - (two_pointers_per_game * 2 * total_games)) / (total_games * 3)
    result = three_pointers_per_game
    return result

print(solution())