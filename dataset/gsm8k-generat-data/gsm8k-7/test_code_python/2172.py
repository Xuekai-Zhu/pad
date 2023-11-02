def solution():
    candles_in_bedroom = 20
    candles_in_living_room = candles_in_bedroom / 2 # Twice the number in the living room
    candles_brought_by_donovan = 20

    # Calculate the total number of candles in the house
    total_candles = candles_in_bedroom + candles_in_living_room + candles_brought_by_donovan
    result = total_candles
    return result

print(solution())