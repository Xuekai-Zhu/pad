def solution():
    gold_bars_found = 100
    friends = 4
    bars_lost = 20
    gold_bars_left = gold_bars_found - bars_lost
    bars_per_friend = gold_bars_left / friends
    result = bars_per_friend
    return result

print(solution())