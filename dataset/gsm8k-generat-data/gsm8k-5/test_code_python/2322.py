def solution():
    # Calculate the total number of touchdowns Richard has scored so far
    td_so_far = 6 * 14  # He has averaged 6 touchdowns in the first 14 games

    # Calculate the number of touchdowns needed to break the record
    td_needed = 90  # Richard needs to score 90 touchdowns to break the record

    # Calculate the number of touchdowns Richard needs to score in the final two games
    td_remaining = td_needed - td_so_far

    # Calculate the average number of touchdowns Richard needs to score in the final two games
    td_per_game = td_remaining / 2

    result = td_per_game
    return result

print(solution())