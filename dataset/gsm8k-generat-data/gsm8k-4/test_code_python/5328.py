def solution():
    """Mona plays a multiplayer video game on the weekends. She joins groups with four other players to complete objectives in the game. The past weekend, she joined 9 groups. One of the groups included two players she had grouped with before that weekend, and another group included one person she had grouped with before. How many unique players did Mona group with on the video game that weekend?"""
    # Define the number of groups Mona joined
    num_groups = 9

    # Define the number of players in each group
    num_players_per_group = 4

    # Calculate the total number of players Mona grouped with
    total_players = num_groups * num_players_per_group

    # Calculate the number of players Mona grouped with multiple times
    repeat_players = 2 + 1

    # Calculate the number of unique players Mona grouped with
    unique_players = total_players - repeat_players

    # Return the result
    result = unique_players
    return result

print(solution())