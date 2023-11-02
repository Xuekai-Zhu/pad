def solution():
    """Daniel works for a sports stadium filling water bottles for athletes. He filled 254 water bottles this season. The football team had 11 players that wanted 6 bottles each. The soccer team had him fill 53 bottles. The lacrosse team needed 12 more bottles than the football team. Each team coach during the season also wanted two bottles apiece. How many bottles did he fill for the rugby team during the final game he worked this season?"""
    total_bottles = 254
    football_players = 11
    football_bottles = 6
    soccer_bottles = 53
    lacrosse_bottles = (football_players * football_bottles) + 12
    coach_bottles = 2 * 4
    total_used_bottles = (football_players * football_bottles) + soccer_bottles + lacrosse_bottles + coach_bottles
    rugby_bottles = total_bottles - total_used_bottles
    result = rugby_bottles
    return result

print(solution())