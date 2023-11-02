def solution():
    """Mona plays a multiplayer video game on the weekends. She joins groups with four other players to complete objectives in the game. The past weekend, she joined 9 groups. One of the groups included two players she had grouped with before that weekend, and another group included one person she had grouped with before. How many unique players did Mona group with on the video game that weekend?"""
    groups_joined = 9
    players_per_group = 4
    players_in_repeated_groups = 3
    unique_players = (groups_joined * players_per_group - players_in_repeated_groups) / players_per_group
    result = unique_players
    return result

print(solution())