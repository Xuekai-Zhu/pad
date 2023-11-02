def solution():
    """Jerry’s two daughters play softball on different teams. They each have 8 games this season. Each team practices 4 hours for every game they play. If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?"""
    # Define the number of games each daughter plays
    games_per_daughter = 8

    # Define the practice time per game
    practice_time = 4

    # Define the game time
    game_time = 2

    # Calculate the total practice time for both daughters
    total_practice_time = (practice_time * games_per_daughter) * 2

    # Calculate the total game time for both daughters
    total_game_time = (game_time * games_per_daughter) * 2

    # Calculate the total time spent at the field
    total_time = total_practice_time + total_game_time

    # return the result
    result = total_time
    return result

print(solution())