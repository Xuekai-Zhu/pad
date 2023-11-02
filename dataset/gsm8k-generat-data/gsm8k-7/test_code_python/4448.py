def solution():
    total_bottles = 254
    football_players = 11
    football_bottles_per_player = 6
    soccer_bottles = 53
    lacrosse_bottles = football_players * football_bottles_per_player + 12
    coach_bottles_per_team = 2

    # Calculate the total number of bottles used by all teams and coaches except rugby
    total_used = (football_players * football_bottles_per_player) + soccer_bottles + lacrosse_bottles + (coach_bottles_per_team * 4)

    # Calculate the number of bottles filled for the rugby team
    rugby_bottles = total_bottles - total_used
    result = rugby_bottles
    return result

print(solution())