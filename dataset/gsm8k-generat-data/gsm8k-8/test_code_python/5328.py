def solution():
    # Calculate the total number of players Mona played with in 9 groups
    total_players = 9 * 4

    # Calculate the number of players she played with multiple times
    repeat_players = 2 + 1

    # Calculate the number of unique players she played with
    unique_players = total_players - repeat_players

    result = unique_players
    return result

print(solution())