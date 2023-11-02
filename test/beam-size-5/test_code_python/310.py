def solution():
    total_players = 105  # The football team has 105 members
    defense_players = total_players / 3  # There are half the number of players on the defense
    offense_players = 2 * defense_players  # There are twice as many players on the offense as there is on the defense
    special_teams_players = defense_players / 2  # There are half the number of players on the special teams as there is on the defense

    # Calculate the number of players on the defense
    defense_players = defense_players - offense_players - special_teams_players
    result = defense_players
    return result

print(solution())