def solution():
    """Jerry’s two daughters play softball on different teams. They each have 8 games this season. Each team practices 4 hours for every game they play. If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?"""
    games_daughter_1 = 8
    games_daughter_2 = 8
    practice_hours_per_game = 4
    game_hours = 2
    hours_daughter_1 = games_daughter_1 * (practice_hours_per_game + game_hours)
    hours_daughter_2 = games_daughter_2 * (practice_hours_per_game + game_hours)
    total_hours = hours_daughter_1 + hours_daughter_2
    result = total_hours
    return result

print(solution())