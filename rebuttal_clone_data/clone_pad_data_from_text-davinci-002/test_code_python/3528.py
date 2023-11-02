def solution():
    water_bottles = 48
    players = 11
    bottles_consumed = players * 2 + players
    bottles_remaining = water_bottles - bottles_consumed
    result = bottles_remaining
    return result

print(solution())