def solution():
    # Mona joins 9 groups with 4 other players each, for a total of 9*4 = 36 players in those groups
    # One group includes 2 players she had grouped with before, so count those players twice
    # Another group includes 1 player she had grouped with before, so count that player once
    # Subtract these players from the total count to get the number of unique players Mona grouped with
    unique_players = 36 - (2 + 1)

    result = unique_players
    return result

print(solution())