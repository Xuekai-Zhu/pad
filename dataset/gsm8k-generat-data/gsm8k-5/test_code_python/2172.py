def solution():
    candles_in_living_room = 20 / 2  # Kalani has twice the number of candles in the living room
    candles_in_bedroom = 20 + candles_in_living_room  # Kalani has 20 candles in the bedroom in addition to those in the living room
    total_candles = candles_in_living_room + candles_in_bedroom + 20  # Donovan brings in 20 more candles

    result = total_candles
    return result

print(solution())