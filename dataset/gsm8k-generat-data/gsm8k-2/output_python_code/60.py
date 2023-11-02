def solution():
    """Jerry’s two daughters play softball on different teams. They each have 8 games this season. Each team practices 4 hours for every game they play. If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?"""
    games_per_daughter = 8
    practice_time_per_game = 4
    game_time = 2
    total_games = games_per_daughter * 2
    total_practice_time = total_games * practice_time_per_game
    total_game_time = total_games * game_time
    total_time = total_game_time + total_practice_time
    result = total_time
    return result

print(solution())