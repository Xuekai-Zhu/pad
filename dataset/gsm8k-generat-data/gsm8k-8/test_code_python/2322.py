def solution():
    # Calculate the total number of touchdowns Archie threw
    archie_touchdowns = 89

    # Calculate the total number of touchdowns Richard has thrown so far
    richard_touchdowns_so_far = 14 * 6

    # Calculate the number of touchdowns Richard needs to break the record
    touchdowns_needed = archie_touchdowns - richard_touchdowns_so_far

    # Calculate the number of games Richard has left to play
    games_left = 16 - 14

    # Calculate the average number of touchdowns Richard needs to throw per game in the final two games
    touchdowns_per_game_needed = touchdowns_needed / games_left
    result = touchdowns_per_game_needed
    return result

print(solution())