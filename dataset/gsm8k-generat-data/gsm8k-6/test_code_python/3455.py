def solution():
    # Calculate the number of cakes and candles
    remaining_cakes = 8 - 2  # Sunny gives away 2 cakes so she has 8 - 2 = 6 remaining cakes
    total_candles = remaining_cakes * 6  # Sunny puts 6 candles on each cake so the total number of candles is remaining_cakes * 6

    result = total_candles
    return result

print(solution())