def solution():
    cakes_baked = 8  # Sunny bakes 8 cakes
    cakes_given_away = 2  # Sunny gives away 2 cakes
    cakes_remaining = cakes_baked - cakes_given_away  # Sunny has some cakes remaining

    candles_per_cake = 6  # Sunny puts 6 candles on each cake

    # Calculate the total number of candles Sunny will use
    total_candles = candles_per_cake * cakes_remaining
    result = total_candles
    return result

print(solution())