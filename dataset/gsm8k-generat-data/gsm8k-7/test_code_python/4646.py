def solution():
    current_yards = 4200
    record_yards = 5999
    games_left = 6

    # Calculate the number of yards Tom Brady needs to pass to beat the record
    yards_to_pass_record = record_yards - current_yards

    # Calculate the average number of yards Brady needs to pass per game
    avg_yards_per_game = yards_to_pass_record / games_left
    result = avg_yards_per_game
    return result

print(solution())