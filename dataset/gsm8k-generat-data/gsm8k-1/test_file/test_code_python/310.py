def solution():
    """A football team has 105 members. There are twice as many players on the offense as there is on the defense. There is half the number of players on the special teams as there is on the defense. How many players are on the defense?"""
    total_players = 105
    offense_players = 2 * defense_players
    special_teams_players = defense_players / 2
    defense_players = (total_players / 3) - (offense_players + special_teams_players)
    result = defense_players
    return result

print(solution())