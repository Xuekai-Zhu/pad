def solution():
     total_candles = 40
     alyssa_candles = total_candles / 2
     remaining_candles = total_candles - alyssa_candles
     chelsea_candles = remaining_candles * 0.7
     candles_in_room = remaining_candles - chelsea_candles
     result = candles_in_room
     return result

print(solution())