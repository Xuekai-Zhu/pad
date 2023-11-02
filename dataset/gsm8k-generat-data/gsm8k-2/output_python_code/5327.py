def solution():
    """Mona plays a multiplayer video game on the weekends. She joins groups with four other players to complete objectives in the game. The past weekend, she joined 9 groups. One of the groups included two players she had grouped with before that weekend, and another group included one person she had grouped with before. How many unique players did Mona group with on the video game that weekend?"""
    total_groups = 9
    players_per_group = 4
    repeated_players = 3
    unique_players = total_groups * players_per_group - repeated_players
    result = unique_players
    return result

print(solution())