def solution():
    """Jerry’s two daughters play softball on different teams. They each have 8 games this season. Each team practices 4 hours for every game they play. If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?"""
    # Define the number of games and hours of practice per game
    games_per_daughter = 8
    practice_hours_per_game = 4
    game_hours = 2

    # Calculate the total hours of practice per daughter
    practice_hours_per_daughter = games_per_daughter * practice_hours_per_game

    # Calculate the total hours of games and practice for both daughters
    total_hours_per_daughter = practice_hours_per_daughter + (games_per_daughter * game_hours)
    total_hours = total_hours_per_daughter * 2

    # Add the hours Jerry spends watching his daughters play to the total
    jerry_hours = games_per_daughter * game_hours * 2
    total_hours += jerry_hours

    # return the result
    result = total_hours
    return result

print(solution())