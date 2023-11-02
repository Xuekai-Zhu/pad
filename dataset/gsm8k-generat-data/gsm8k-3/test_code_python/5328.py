def solution():
    """Mona joins groups with four other players to complete objectives in a multiplayer video game. The past weekend, she joined 9 groups. One of the groups included two players she had grouped with before that weekend, and another group included one person she had grouped with before. How many unique players did Mona group with on the video game that weekend?"""
    # Define the number of groups Mona joined
    num_groups = 9

    # Define the number of players in each group, including Mona
    num_players_per_group = 5

    # Define the number of players Mona had previously grouped with
    num_previous_players = 3

    # Calculate the total number of players Mona grouped with
    total_players = num_groups * num_players_per_group - num_previous_players

    # Display the total number of unique players Mona grouped with
    result = total_players
    return result

print(solution())