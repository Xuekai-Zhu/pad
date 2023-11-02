def solution():
    # Calculate how many touchdowns Richard has already scored in the first 14 games
    touchdowns_so_far = 6 * 14
    # Calculate how many more touchdowns Richard needs to beat Archie's record
    remaining_touchdowns = 89 - touchdowns_so_far
    # Calculate how many touchdowns per game Richard needs to score in the final two games
    touchdowns_per_game_needed = remaining_touchdowns / 2
    result = touchdowns_per_game_needed
    return result

print(solution())