def solution():
    """Daniel works for a sports stadium filling water bottles for athletes. He filled 254 water bottles this season. The football team had 11 players that wanted 6 bottles each. The soccer team had him fill 53 bottles. The lacrosse team needed 12 more bottles than the football team. Each team coach during the season also wanted two bottles apiece. How many bottles did he fill for the rugby team during the final game he worked this season?"""
    # Define the number of bottles each football player wanted
    FOOTBALL_PLAYER_BOTTLES = 6

    # Define the number of bottles each coach wanted
    COACH_BOTTLES = 2

    # Calculate the number of bottles filled for the football team
    football_players = 11
    football_team_bottles = football_players * FOOTBALL_PLAYER_BOTTLES
    football_coach_bottles = COACH_BOTTLES
    total_football_bottles = football_team_bottles + football_coach_bottles

    # Calculate the number of bottles filled for the soccer team
    soccer_bottles = 53
    soccer_coach_bottles = COACH_BOTTLES

    # Calculate the number of bottles filled for the lacrosse team
    lacrosse_players = 11
    lacrosse_team_bottles = football_team_bottles + 12
    lacrosse_coach_bottles = COACH_BOTTLES
    total_lacrosse_bottles = lacrosse_team_bottles + lacrosse_coach_bottles

    # Calculate the total number of bottles filled
    total_bottles = football_team_bottles + football_coach_bottles + soccer_bottles + soccer_coach_bottles + total_lacrosse_bottles

    # Calculate the number of bottles filled for the rugby team
    rugby_bottles = 254 - total_bottles

    # Display the number of bottles filled for the rugby team
    result = rugby_bottles
    return result

print(solution())