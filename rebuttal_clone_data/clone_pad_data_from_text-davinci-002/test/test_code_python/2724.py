def solution():
    total_players = 40
    never_lost = total_players / 4
    lost_once = total_players - never_lost
    result = lost_once
    return result

print(solution())