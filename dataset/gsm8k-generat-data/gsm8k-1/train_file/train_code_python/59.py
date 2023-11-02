def solution():
    """Jerry’s two daughters play softball on different teams. They each have 8 games this season. Each team practices 4 hours for every game they play. If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?"""
    games_per_daughter = 8
    practice_hours_per_game = 4
    game_hours = 2
    total_games = games_per_daughter * 2 # Two daughters
    total_practice_hours = total_games * practice_hours_per_game
    total_game_hours = total_games * game_hours
    total_hours = total_practice_hours + total_game_hours
    result = total_hours
    return result

print(solution())