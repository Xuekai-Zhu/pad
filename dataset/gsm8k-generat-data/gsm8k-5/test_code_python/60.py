def solution():
    num_games = 8  # Each daughter has 8 games so there are a total of 16 games
    practice_time = 4  # Each team practices for 4 hours before each game
    game_time = 2  # Each game lasts 2 hours

    # Calculate the total time spent at the field for each daughter (practice + game time)
    daughter_time = (num_games * (practice_time + game_time))

    # Calculate the total time spent at the field for both daughters
    total_time = daughter_time * 2
    result = total_time
    return result

print(solution())