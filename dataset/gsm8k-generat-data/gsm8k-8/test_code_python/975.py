def solution():
    games_played = 20 * 0.8
    fouls_per_game = 5
    free_throws_per_foul = 2
    free_throw_percentage = 0.7

    total_fouls = games_played * fouls_per_game
    total_free_throws = total_fouls * free_throws_per_foul
    successful_free_throws = total_free_throws * free_throw_percentage

    result = successful_free_throws
    return result

print(solution())