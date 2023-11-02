def solution():
    grandfather_age = 79  # Caleb's grandfather is turning 79 years old
    yellow_candles = 27  # Caleb puts 27 yellow candles on the cake
    red_candles = 14  # Caleb puts 14 red candles on the cake

    # Calculate the number of blue candles Caleb used
    blue_candles = grandfather_age - yellow_candles - red_candles
    result = blue_candles
    return result

print(solution())