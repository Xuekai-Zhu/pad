def solution():
    
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