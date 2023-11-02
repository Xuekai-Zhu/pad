def solution():
    total_bottles = 254  # Daniel filled 254 water bottles this season
    football_players = 11
    football_bottles_per_player = 6
    soccer_bottles = 53
    lacrosse_bottles = football_players * football_bottles_per_player + 12
    total_team_bottles = (football_players * football_bottles_per_player + 2) + 2 + 2  # Each team coach wanted 2 bottles

    # Calculate the number of bottles filled for the rugby team during the final game
    rugby_bottles = total_bottles - soccer_bottles - lacrosse_bottles - total_team_bottles
    result = rugby_bottles
    return result

print(solution())