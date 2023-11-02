def solution():
    cakes_baked = 8
    cakes_given_away = 2
    candles_per_cake = 6
    candles_used = (cakes_baked - cakes_given_away) * candles_per_cake
    result = candles_used
    return result

print(solution())