def solution():
    # Let's assign the number of games won by Dana as "d"
    # Perry won 5 more games than Dana, so he won "d + 5" games
    # Charlie won 2 fewer games than Dana, so he won "d - 2" games
    # Phil won 3 more games than Charlie, so he won "d - 2 + 3" = "d + 1" games
    # We know that Phil won 12 games in total, so "d + 1" = 12 => d = 11
    # Therefore, Dana won 11 games, Perry won 16 games (11 + 5), Charlie won 9 games (11 - 2), and Phil won 12 games

    perry_wins = 16
    phil_wins = 12

    # Calculate the difference in the number of wins between Perry and Phil
    difference = perry_wins - phil_wins
    result = difference
    return result

print(solution())